#!/usr/bin/env/python3

import os
import re
import sys
import json
import time
import os.path
import subprocess

from dataclasses       import dataclass,    field,       asdict

from PySide2.QtCore    import Qt,           QTimer    
from PySide2.QtGui     import QTextCursor,  QPalette,    QColor,      QTextCharFormat, QPixmap
from PySide2.QtWidgets import QApplication, QMainWindow, QListWidget, QGraphicsScene, QGraphicsPixmapItem, QDialog, QTextEdit, QPushButton, QMessageBox 

sys.path.insert(1, './QWindows')

from StartWindow       import Ui_StartWindow
from Users             import Ui_Users
from AddUser           import Ui_AddUser
from ListWindow        import Ui_ListWindow
from LevelWindow       import Ui_LevelWindow
from ColemakKeyboard   import Ui_ColemakKeyboard
    

@dataclass
class User:
    name:             str       = "None"
    keyboardLayout:   str       = "QWERTY"
    keyboardLanguage: str       = "us"
    levelsErrors:     list[int] = field(default_factory=list)
    finishedLevels:   int       = 0


class ColemakKeyboard(QMainWindow, Ui_ColemakKeyboard):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttons = self.findChildren(QPushButton)


class LevelWindow(QMainWindow, Ui_LevelWindow):
    def __init__(self, main):
        super().__init__()
        self.setupUi(self)

        self.mainWindow             = main
        self.user                   = main.choseUser.user
        
        self.levelText              = QTextEdit()
        self.textIndex              = -1
        self.errorCounter           = 0

        with open(f"./Levels/{main.levelsList.levelName}.json", "r") as f:
            load = json.load(f)
            self.levelText.setText(load[self.user.keyboardLayout])
            self.maxErrors          = load["maxErrors"]
        self.levelText.setReadOnly(True)
        self.scrollArea.setWidget(self.levelText)
        
        self.textEdit.setFocus()
        
        self.buttonsList            = self.findChildren(QPushButton)
        self.colemakButtons         = ColemakKeyboard()
        self.colemakButtonsList     = self.colemakButtons.buttons
        if self.user.keyboardLayout == "Colemak":
            self.buttonsList        = sorted(self.buttonsList, key=lambda x: x.objectName())
            self.colemakButtonsList = sorted(self.colemakButtonsList, key=lambda x: x.objectName())
            for i, j in zip(self.buttonsList, self.colemakButtonsList): i.setText(j.text())

        self.nextSymbol()
        self.textEdit.textChanged.connect(self.userStartPrinted)

        self.timer                  = QTimer()
        self.isScreenColored        = False
        self.timer.timeout.connect(self.coloringScreen)

    def highlightSymbol(self):
        if self.levelText.toPlainText()[self.textIndex] != "\n":
            text = self.levelText.toPlainText().replace("\n", "<br/>")
            if self.textIndex + 1 == len(text):
                self.levelText.setText(f"{text[:self.textIndex]}<span style='background-color: gray'>{text[self.textIndex]}</span>")
            else:
                self.levelText.setText(f"{text[:self.textIndex]}<span style='background-color: gray'>{text[self.textIndex]}</span>{text[self.textIndex+1:]}\n")

    def highlightKeyboardButton(self):
        symbol = self.levelText.toPlainText()[self.textIndex]
        for i in self.buttonsList:
            i.setStyleSheet("background-color: white")

            if symbol.isupper():
                self.Btn42.setStyleSheet("background-color: gray")
                self.Btn53.setStyleSheet("background-color: gray")
                symbol = symbol.lower()

            if symbol == " ":
                self.Btn57.setStyleSheet("background-color: gray")

            if symbol == "\n":
                self.Btn41.setStyleSheet("background-color: gray")

            if symbol == i.text():
                i.setStyleSheet("background-color: grey")

    def nextSymbol(self):
        self.textIndex += 1
        self.highlightSymbol()
        self.highlightKeyboardButton()

    def coloringScreen(self):
        self.timer.stop()
        if self.isScreenColored:
            self.setStyleSheet("background-color: white")
            
            self.textEdit.setReadOnly(False)
            self.textEdit.setFocus()
            
            self.isScreenColored = False
        else:
            if self.errorCounter > self.maxErrors or not self.errorCounter:
                self.setStyleSheet("background-color: black")
            elif self.errorCounter == self.maxErrors:
                self.setStyleSheet("background-color: red")
            elif 0 < self.errorCounter < self.maxErrors:
                self.setStyleSheet("background-color: yellow")
            
            self.textEdit.setReadOnly(True)

            self.isScreenColored = True
            self.timer.start(1000)

    def userMadeError(self):
        self.errorCounter      += 1
        self.timer.start(1)
        if self.errorCounter > self.maxErrors:
            self.errorCounter   = 0
            self.textIndex      = -1
            self.textEdit.setText("")
            self.nextSymbol()
        else:
            text = self.textEdit.toPlainText()
            if text.count("\n") > 1:
                self.textEdit.setText(text[:text.rfind("\n")+1])
                self.textIndex -= text.rfind("\n")-1
            else:
                self.textEdit.setText("")
                self.textIndex  = -1
            self.nextSymbol()

    def userStartPrinted(self):
        if self.textEdit.toPlainText():
            symbol = self.textEdit.toPlainText()[-1]
            if symbol == self.levelText.toPlainText()[self.textIndex]:
                if self.textIndex == len(self.levelText.toPlainText())-1:
                    QMessageBox.about(self, "Gratulations!!!", "You Finished the level!")

                    levelIndex = int(self.mainWindow.levelsList.levelName[-1])
                    
                    if levelIndex >= self.mainWindow.choseUser.user.finishedLevels: self.mainWindow.choseUser.user.finishedLevels += 1

                    if levelIndex > len(self.mainWindow.choseUser.user.levelsErrors):
                        self.mainWindow.choseUser.user.levelsErrors.append(self.errorCounter)
                    else: self.mainWindow.choseUser.user.levelsErrors[levelIndex-1] = self.errorCounter

                    self.mainWindow.saveProgress()
                    self.close()
                    self.mainWindow.levelsList.show()
                    self.destroy()
                    self.mainWindow.levelsList.checkLevelsList()

                else: self.nextSymbol()
            else: self.userMadeError()


class LevelsListWindow(QMainWindow, Ui_ListWindow):
    def __init__(self, main):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(311, 494)

        self.mainWindow = main

        os.chdir("./Levels")
        self.levelsList = re.findall(r'[\w ]+', subprocess.run('ls', capture_output=True, shell=True).stdout.decode('utf-8'))[::2]
        self.levelsList = sorted(self.levelsList, key=lambda x: int(re.search("[\d]+", x)[0]))
        os.chdir("..")

        self.levels     = QListWidget()
        self.levels.addItems(self.levelsList)
        self.scrollArea.setWidget(self.levels)

        self.startButton.setEnabled(False)

        self.levels.itemClicked.connect(self.levelSelected)
        self.startButton.clicked.connect(self.startLevel)
        self.backButton.clicked.connect(self.getBack)

        self.checkLevelsList()

    def checkLevelsList(self):
        if self.mainWindow.choseUser.user.levelsErrors != []:
            levelsCopy = self.levelsList.copy()
            for i in range(len(self.mainWindow.choseUser.user.levelsErrors)):
                levelsCopy[i] += f"\tErrors: {self.mainWindow.choseUser.user.levelsErrors[i]}"
            self.levels.clear()
            self.levels.addItems(levelsCopy)
            self.scrollArea.setWidget(self.levels)
        
        if sum(self.mainWindow.choseUser.user.levelsErrors) >= GLOBAL_MAX_ERRORS:
            QMessageBox.about(self, "Overlimit", "Passing the levels, you made too many mistakes in total. Please reread them.")

            for i in self.mainWindow.choseUser.user.levelsErrors: 
                if i > 0: break

            index = self.mainWindow.choseUser.user.levelsErrors.index(i)

            self.mainWindow.choseUser.user.finishedLevels  = index

            self.mainWindow.choseUser.user.levelsErrors    = self.mainWindow.choseUser.user.levelsErrors[:index + 1]
            self.mainWindow.saveProgress()   

    def getBack(self):
        self.close()
        self.mainWindow.choseUser.show()
        self.destroy()

    def levelSelected(self, item):
        self.user      = self.mainWindow.choseUser.user
        self.levelName = item.text()
        if self.levelName.count("\t"): self.levelName = self.levelName[:self.levelName.find("\t")]
        if int(re.search("[\d]+", item.text())[0]) - 1 <= self.user.finishedLevels: self.startButton.setEnabled(True)
        else: self.startButton.setEnabled(False)

    def startLevel(self, item):
        self.mainWindow.level = LevelWindow(self.mainWindow)
        self.mainWindow.level.showMaximized()
        self.hide()
        self.mainWindow.programsIds.append(getActivedWindowId())


class AddUserDialog(QDialog, Ui_AddUser):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.user = None

        self.comboBox.addItem("QWERTY")
        self.comboBox.addItem("Colemak")

        self.buttonBox.clicked.connect(self.accept)

        self.show()

    def accept(self, button):
        if self.lineEdit.text():
            self.user  = User(self.lineEdit.text(), self.comboBox.currentText())
            super().accept()
        else: 
            pal = self.lineEdit.palette()
            text_color = QColor("red")
            pal.setColor(QPalette.PlaceholderText, text_color)
            self.lineEdit.setPalette(pal)
        

class ChooseUser(QMainWindow, Ui_Users):
    def __init__(self, main):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(300, 400)

        self.mainWindow = main
        self.user       = User()

        os.chdir("./Users")
        self.usersList  = re.findall(r'[\w]+', subprocess.run('ls', capture_output=True, shell=True).stdout.decode('utf-8'))[::2]
        os.chdir("..")

        self.users      = QListWidget()
        self.updateUsersList()

        self.startButton.setEnabled(False)
        
        self.users.itemClicked.connect(self.selectedUser)
        self.startButton.pressed.connect(self.start)
        self.addNewUserButton.pressed.connect(self.addNewUser)
        self.BackButton.pressed.connect(self.getBack)

    def getBack(self):
        self.close()
        self.mainWindow.show()

    def selectedUser(self, item):
        self.startButton.setEnabled(True)
        with open(f"./Users/{item.text()}.json", "r") as f:
            self.user = User(**json.load(f))

    def start(self):
        self.mainWindow.levelsList = LevelsListWindow(self.mainWindow)
        self.mainWindow.levelsList.show()
        self.hide()
        self.mainWindow.programsIds.append(getActivedWindowId())

    def addNewUser(self):
        dialog = AddUserDialog()
        self.addNewUserButton.setEnabled(False)
        self.startButton.setEnabled(False)
        dialog.exec_()

        self.addNewUserButton.setEnabled(True)
        with open(f"./Users/{dialog.user.name}.json", "w") as f:
            json.dump(asdict(dialog.user), f)

        self.usersList.append(dialog.user.name)
        self.updateUsersList()

    def updateUsersList(self): 
        self.users.clear()
        self.users.addItems(self.usersList)
        self.scrollArea.setWidget(self.users)


class MainWindow(QMainWindow, Ui_StartWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(300, 400)
        self.programsIds = []
        self.show()
        self.programsIds.append(getActivedWindowId())

        pix              = QPixmap("./Logo.png")
        item             = QGraphicsPixmapItem(pix)
        scene            = QGraphicsScene(self)
        scene.addItem(item)
        self.graphicsView.setScene(scene)

        self.choseUser   = ChooseUser(self)

        self.timer       = QTimer(self)
        self.timer.timeout.connect(self.timeCount)
        self.timer.start(1000)

        self.startButton.pressed.connect(self.start)
        self.exitButton.pressed.connect(self.nigerundayo)

    def nigerundayo(self):
        self.close()
        self.destroy()

    def timeCount(self):
        if not isThisProgramActived(self.programsIds) and getActivedKeyboardLanguage() != USER_DEFAULT_LANGUAGES:
            changeKeyboardLayout(USER_DEFAULT_LANGUAGES)
        elif   isThisProgramActived(self.programsIds) and getActivedKeyboardLanguage() != f"{self.choseUser.user.keyboardLanguage}":
            changeKeyboardLayout(self.choseUser.user.keyboardLanguage, self.choseUser.user.keyboardLayout)

    def start(self):
        self.choseUser.show()
        self.hide()
        self.programsIds.append(getActivedWindowId())

    def saveProgress(self):
        with open(f"./Users/{self.choseUser.user.name}.json", "w") as f:
            json.dump(asdict(self.choseUser.user), f)

def getActivedWindowId(): return subprocess.run('xdotool getactivewindow', shell=True, capture_output=True).stdout.decode('utf-8')

def getActivedKeyboardLanguage() -> str: 
    ret = subprocess.run("setxkbmap -print | grep xkb_symbols | awk '{print $4}'", shell=True, capture_output=True).stdout.decode("utf-8")
    ret = re.sub(r":.", "", re.search("\+.*\+", ret)[0][:-1])
    return ret[ret.find("+")+1:ret.rfind("+")].replace("+", ",")

def isThisProgramActived(programsIds) -> bool:
    return getActivedWindowId() in programsIds

def changeKeyboardLayout(language: str="us", layout: str="qwerty") -> None:
    if language != getActivedKeyboardLanguage():
        if layout   == "qwerty": subprocess.run(f'setxkbmap {language}; xset -r 66', shell=True)
        elif layout == "Colemak": subprocess.run(f'setxkbmap us; xmodmap ./KeyboardLayouts/xmodmap.colemak && xset r 66', shell=True)

if __name__ == "__main__":
    app                    = QApplication(sys.argv)
    ui                     = MainWindow()
    USER_DEFAULT_LANGUAGES = getActivedKeyboardLanguage()
    GLOBAL_MAX_ERRORS      = 9
    app.exec_()
    changeKeyboardLayout(USER_DEFAULT_LANGUAGES)

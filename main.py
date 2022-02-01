import sys

from PySide2.QtCore import Qt, QTimer
from PySide2.QtWidgets import QApplication, QMainWindow

from MainWindow import Ui_MainWindow
from StartWindow import Ui_StartWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        
        self.chalennge = "n n n n n n n n n n n n"
        self.pattern = "<span style='background-color: gray'>{}</span>"
        self.errPattern = "errors: {}"
        self.isScreenRed = False

        self.simbolIndex = 0
        self.errCount = 0

        self.timer = QTimer()

        self.ToNaber.setText(self.nextSimbol())
        self.ErrCount.setText(self.errPattern.format(self.errCount))
        self.textEdit.textChanged.connect(self.textWillChanged)
        self.timer.timeout.connect(self.givedError)

    def textWillChanged(self):
        text = self.textEdit.toPlainText()[-1:]
        if text:
            if self.simbolIndex != len(self.chalennge) -1:
                if text == self.chalennge[self.simbolIndex]:
                    self.simbolIndex += 1
                    self.ToNaber.setText(self.nextSimbol())
                else:
                    self.errCount += 1
                    if self.errCount != 3:
                        print(self.errCount)
                        self.ErrCount.setText(self.errPattern.format(self.errCount))
                        self.textEdit.setText(self.textEdit.toPlainText()[:-1])
                    else:
                        self.errCount = 0
                        self.simbolIndex = 0
                        self.textEdit.setText("")
                        self.ToNaber.setText(self.nextSimbol())
                        self.ErrCount.setText(self.errPattern.format(self.errCount))
                    self.timer.start(0.01)
            else:
                self.ToNaber.setText("Well Done!")

        print("Text changed...>>> "+self.textEdit.toPlainText()[-1:])

    def nextSimbol(self):
        t = ""
        for i in range(len(self.chalennge)):
            if i == self.simbolIndex:
                t += self.pattern.format(self.chalennge[i])
            else:
                t += self.chalennge[i]
        return t

    def givedError(self):
        self.timer.stop()
        if self.isScreenRed:
            self.textEdit.setStyleSheet("background-color: white")
            self.isScreenRed = False
        else:
            self.textEdit.setStyleSheet("background-color: red")
            self.isScreenRed = True
            self.timer.start(1000)

class StartWindow(QMainWindow, Ui_StartWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.startButton.pressed.connect(self.push_start)

    def push_start(self):
        self.hide()
        self.window = MainWindow()

app = QApplication(sys.argv)
ui = StartWindow()
app.exec_()

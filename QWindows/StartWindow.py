# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StartWindowaeYgmE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_StartWindow(object):
    def setupUi(self, StartWindow):
        if not StartWindow.objectName():
            StartWindow.setObjectName(u"StartWindow")
        StartWindow.resize(300, 396)
        self.centralwidget = QWidget(StartWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(60, 60, 191, 231))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.graphicsView = QGraphicsView(self.verticalLayoutWidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.verticalLayout.addWidget(self.graphicsView)

        self.startButton = QPushButton(self.verticalLayoutWidget)
        self.startButton.setObjectName(u"startButton")

        self.verticalLayout.addWidget(self.startButton)

        self.settingsButton = QPushButton(self.verticalLayoutWidget)
        self.settingsButton.setObjectName(u"settingsButton")

        self.verticalLayout.addWidget(self.settingsButton)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(130, 360, 161, 32))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 6, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel {\n"
"	font-size: 13px;\n"
"}")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)

        self.checkBox = QCheckBox(self.horizontalLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"QCheckBox::indicator:unchecked {\n"
"        image: url(images/switch_off.png);\n"
"        width: 30px;\n"
"        height: 30px;\n"
"    }\n"
"    QCheckBox::indicator:checked {\n"
"        image: url(images/switch_on.png);\n"
"        width: 30px;\n"
"        height: 30px;\n"
"    }\n"
"QCheckBox {\n"
"	font-size: 13px;\n"
"}")
        self.checkBox.setAutoRepeatDelay(300)

        self.horizontalLayout.addWidget(self.checkBox)

        StartWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StartWindow)

        QMetaObject.connectSlotsByName(StartWindow)
    # setupUi

    def retranslateUi(self, StartWindow):
        StartWindow.setWindowTitle(QCoreApplication.translate("StartWindow", u"StartWindow", None))
        self.startButton.setText(QCoreApplication.translate("StartWindow", u"Start", None))
        self.settingsButton.setText(QCoreApplication.translate("StartWindow", u"Settings", None))
        self.label.setText(QCoreApplication.translate("StartWindow", u"Colemak", None))
        self.checkBox.setText(QCoreApplication.translate("StartWindow", u"QWERTY", None))
    # retranslateUi


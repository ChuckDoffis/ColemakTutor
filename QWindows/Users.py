# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UsersCuRgMZ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Users(object):
    def setupUi(self, Users):
        if not Users.objectName():
            Users.setObjectName(u"Users")
        Users.resize(300, 396)
        self.centralwidget = QWidget(Users)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 281, 381))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 277, 342))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.BackButton = QPushButton(self.verticalLayoutWidget)
        self.BackButton.setObjectName(u"BackButton")

        self.horizontalLayout.addWidget(self.BackButton)

        self.addNewUserButton = QPushButton(self.verticalLayoutWidget)
        self.addNewUserButton.setObjectName(u"addNewUserButton")

        self.horizontalLayout.addWidget(self.addNewUserButton)

        self.startButton = QPushButton(self.verticalLayoutWidget)
        self.startButton.setObjectName(u"startButton")

        self.horizontalLayout.addWidget(self.startButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        Users.setCentralWidget(self.centralwidget)

        self.retranslateUi(Users)

        QMetaObject.connectSlotsByName(Users)
    # setupUi

    def retranslateUi(self, Users):
        Users.setWindowTitle(QCoreApplication.translate("Users", u"MainWindow", None))
        self.BackButton.setText(QCoreApplication.translate("Users", u"Back", None))
        self.addNewUserButton.setText(QCoreApplication.translate("Users", u"Add New User", None))
        self.startButton.setText(QCoreApplication.translate("Users", u"Start", None))
    # retranslateUi


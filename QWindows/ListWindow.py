# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ListWindowQDiDiC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ListWindow(object):
    def setupUi(self, ListWindow):
        if not ListWindow.objectName():
            ListWindow.setObjectName(u"ListWindow")
        ListWindow.resize(311, 494)
        self.centralwidget = QWidget(ListWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 10, 291, 431))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 289, 429))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(160, 450, 141, 41))
        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(10, 450, 141, 41))
        ListWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ListWindow)

        QMetaObject.connectSlotsByName(ListWindow)
    # setupUi

    def retranslateUi(self, ListWindow):
        ListWindow.setWindowTitle(QCoreApplication.translate("ListWindow", u"MainWindow", None))
        self.startButton.setText(QCoreApplication.translate("ListWindow", u"Start", None))
        self.backButton.setText(QCoreApplication.translate("ListWindow", u"Back", None))
    # retranslateUi


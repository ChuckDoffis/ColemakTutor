# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StartWindowtCBVtv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, StartWindow):
        if not StartWindow.objectName():
            StartWindow.setObjectName(u"StartWindow")
        StartWindow.resize(300, 400)
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
        
        StartWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StartWindow)

        QMetaObject.connectSlotsByName(StartWindow)
    # setupUi

    def retranslateUi(self, StartWindow):
        StartWindow.setWindowTitle(QCoreApplication.translate("StartWindow", u"StartWindow", None))
        self.startButton.setText(QCoreApplication.translate("StartWindow", u"Start", None))
    # retranslateUi


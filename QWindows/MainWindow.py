# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledINHbLY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 400)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ToNaber = QLabel(self.centralwidget)
        self.ToNaber.setObjectName(u"ToNaber")
        self.ToNaber.setEnabled(True)
        self.ToNaber.setGeometry(QRect(0, 180, 301, 121))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToNaber.sizePolicy().hasHeightForWidth())
        self.ToNaber.setSizePolicy(sizePolicy)
        self.ToNaber.setStyleSheet(u"p {\n"
"  display: inline;\n"
"}")
        self.ToNaber.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(0, 0, 301, 171))
        self.ErrCount = QLabel(self.centralwidget)
        self.ErrCount.setObjectName(u"ErrCount")
        self.ErrCount.setGeometry(QRect(230, 150, 66, 19))
        self.ErrCount.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Proba", None))
        self.ToNaber.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.ErrCount.setText(QCoreApplication.translate("MainWindow", u"errors: 0", None))
    # retranslateUi


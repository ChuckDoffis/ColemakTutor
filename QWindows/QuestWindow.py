# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QuestWindowyItypy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_QuestWindow(object):
    def setupUi(self, QuestWindow):
        if not QuestWindow.objectName():
            QuestWindow.setObjectName(u"QuestWindow")
        QuestWindow.resize(300, 130)
        self.horizontalLayoutWidget = QWidget(QuestWindow)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 90, 301, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.colemakBtn = QPushButton(self.horizontalLayoutWidget)
        self.colemakBtn.setObjectName(u"colemakBtn")

        self.horizontalLayout.addWidget(self.colemakBtn)

        self.qwertyBtn = QPushButton(self.horizontalLayoutWidget)
        self.qwertyBtn.setObjectName(u"qwertyBtn")

        self.horizontalLayout.addWidget(self.qwertyBtn)

        self.label = QLabel(QuestWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 300, 100))
        self.label.setStyleSheet(u"QLabel {\n"
"	font-size: 20px;\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(QuestWindow)

        QMetaObject.connectSlotsByName(QuestWindow)
    # setupUi

    def retranslateUi(self, QuestWindow):
        QuestWindow.setWindowTitle(QCoreApplication.translate("QuestWindow", u"Dialog", None))
        self.colemakBtn.setText(QCoreApplication.translate("QuestWindow", u"Colemak", None))
        self.qwertyBtn.setText(QCoreApplication.translate("QuestWindow", u"QWERTY", None))
        self.label.setText(QCoreApplication.translate("QuestWindow", u"Which one keyboard layout \n"
"you will use?", None))
    # retranslateUi


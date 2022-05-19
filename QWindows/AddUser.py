# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddUserIumGQz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AddUser(object):
    def setupUi(self, AddUser):
        if not AddUser.objectName():
            AddUser.setObjectName(u"AddUser")
        AddUser.resize(380, 115)
        self.buttonBox = QDialogButtonBox(AddUser)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(180, 70, 171, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.comboBox = QComboBox(AddUser)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(30, 70, 141, 31))
        self.horizontalLayoutWidget = QWidget(AddUser)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 10, 321, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.retranslateUi(AddUser)
        self.buttonBox.rejected.connect(AddUser.reject)

        QMetaObject.connectSlotsByName(AddUser)
    # setupUi

    def retranslateUi(self, AddUser):
        AddUser.setWindowTitle(QCoreApplication.translate("AddUser", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("AddUser", u"Name:", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("AddUser", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u043d\u043e\u0432\u043e\u0433\u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
    # retranslateUi


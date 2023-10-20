# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'keypoint_number_dialogGddbuG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dialog(object):
    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.resize(448, 300)
        self.verticalLayout = QVBoxLayout(dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.classesList = QListWidget(dialog)
        self.classesList.setObjectName(u"classesList")

        self.verticalLayout.addWidget(self.classesList)

        self.numberEdit = QLineEdit(dialog)
        self.numberEdit.setObjectName(u"numberEdit")

        self.verticalLayout.addWidget(self.numberEdit)

        self.frame = QFrame(dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.okButton = QPushButton(self.frame)
        self.okButton.setObjectName(u"okButton")

        self.horizontalLayout.addWidget(self.okButton)

        self.cancelButton = QPushButton(self.frame)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)


        self.verticalLayout.addWidget(self.frame)

        QWidget.setTabOrder(self.classesList, self.numberEdit)
        QWidget.setTabOrder(self.numberEdit, self.okButton)
        QWidget.setTabOrder(self.okButton, self.cancelButton)

        self.retranslateUi(dialog)
        self.cancelButton.clicked.connect(dialog.reject)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("dialog", u"\u6570\u636e\u96c6\u5173\u952e\u70b9\u6570\u91cf", None))
        self.label.setText(QCoreApplication.translate("dialog", u"<html><head/><body><p>\u8bf7\u5728\u4e0b\u65b9\u7684\u5217\u8868\u4e2d\uff0c\u9009\u62e9\u4f60\u9700\u8981\u68c0\u67e5\u7684\u7c7b\u522b\uff0c</p><p>\u5e76\u5728\u6587\u672c\u6846\u5185\u8f93\u5165\u8fd9\u4e2a\u7c7b\u522b\u5173\u952e\u70b9\u5e94\u6709\u7684\u6570\u91cf</p></body></html>", None))
        self.okButton.setText(QCoreApplication.translate("dialog", u"\u786e\u8ba4", None))
        self.cancelButton.setText(QCoreApplication.translate("dialog", u"\u53d6\u6d88", None))
    # retranslateUi


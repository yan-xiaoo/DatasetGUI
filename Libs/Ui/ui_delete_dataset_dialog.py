# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delete_dataset_dialogKpjsZO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 151)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textLabel = QLabel(Dialog)
        self.textLabel.setObjectName(u"textLabel")
        font = QFont()
        font.setPointSize(17)
        self.textLabel.setFont(font)

        self.verticalLayout.addWidget(self.textLabel)

        self.detailLabel = QLabel(Dialog)
        self.detailLabel.setObjectName(u"detailLabel")

        self.verticalLayout.addWidget(self.detailLabel)

        self.clearFileBox = QCheckBox(Dialog)
        self.clearFileBox.setObjectName(u"clearFileBox")

        self.verticalLayout.addWidget(self.clearFileBox)

        self.frame = QFrame(Dialog)
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


        self.retranslateUi(Dialog)
        self.cancelButton.clicked.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u5220\u9664\u786e\u8ba4", None))
        self.textLabel.setText(QCoreApplication.translate("Dialog", u"\u786e\u8ba4\u8981\u5220\u9664\u540d\u4e3a\u2026\u7684\u6570\u636e\u96c6\u5417\uff1f", None))
        self.detailLabel.setText(QCoreApplication.translate("Dialog", u"\u5982\u679c\u60a8\u4e0d\u9009\u62e9\u201c\u6e05\u9664\u6570\u636e\u96c6\u6587\u4ef6\u201d\uff0c\u5219\u6570\u636e\u96c6\u672c\u8eab\u4e0d\u4f1a\u4e22\u5931", None))
        self.clearFileBox.setText(QCoreApplication.translate("Dialog", u"\u540c\u65f6\u6e05\u9664\u6570\u636e\u96c6\u6587\u4ef6", None))
        self.okButton.setText(QCoreApplication.translate("Dialog", u"\u786e\u8ba4", None))
        self.cancelButton.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi


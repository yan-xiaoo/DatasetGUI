# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'check_result_dialoggpcAvO.ui'
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
        Dialog.resize(518, 300)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.numberLabel = QLabel(Dialog)
        self.numberLabel.setObjectName(u"numberLabel")
        font1 = QFont()
        font1.setPointSize(17)
        self.numberLabel.setFont(font1)

        self.verticalLayout.addWidget(self.numberLabel)

        self.detailLabel = QLabel(Dialog)
        self.detailLabel.setObjectName(u"detailLabel")

        self.verticalLayout.addWidget(self.detailLabel)

        self.problemList = QListWidget(Dialog)
        self.problemList.setObjectName(u"problemList")
        self.problemList.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout.addWidget(self.problemList)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.expandButton = QPushButton(self.frame)
        self.expandButton.setObjectName(u"expandButton")

        self.horizontalLayout.addWidget(self.expandButton)

        self.confirmButton = QPushButton(self.frame)
        self.confirmButton.setObjectName(u"confirmButton")

        self.horizontalLayout.addWidget(self.confirmButton)

        self.cleanButton = QPushButton(self.frame)
        self.cleanButton.setObjectName(u"cleanButton")

        self.horizontalLayout.addWidget(self.cleanButton)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)
        self.confirmButton.clicked.connect(Dialog.accept)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u68c0\u67e5\u7ed3\u679c", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u6570\u636e\u96c6\u68c0\u67e5\u7ed3\u679c", None))
        self.numberLabel.setText(QCoreApplication.translate("Dialog", u"\u6570\u636e\u96c6\u4e2d\u5b58\u5728 2 \u9879\u95ee\u9898", None))
        self.detailLabel.setText(QCoreApplication.translate("Dialog", u"\u5177\u4f53\u5185\u5bb9", None))
        self.expandButton.setText(QCoreApplication.translate("Dialog", u"\u5c55\u5f00", None))
        self.confirmButton.setText(QCoreApplication.translate("Dialog", u"\u8fd4\u56de", None))
        self.cleanButton.setText(QCoreApplication.translate("Dialog", u"\u6267\u884c\u6e05\u7406", None))
    # retranslateUi


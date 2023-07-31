# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delete_problemBTmWSJ.ui'
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
        Dialog.resize(435, 200)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.whyButton = QPushButton(self.frame)
        self.whyButton.setObjectName(u"whyButton")

        self.gridLayout.addWidget(self.whyButton, 0, 0, 1, 1)

        self.cancelButton = QPushButton(self.frame)
        self.cancelButton.setObjectName(u"cancelButton")

        self.gridLayout.addWidget(self.cancelButton, 0, 3, 1, 1)

        self.imageButton = QPushButton(self.frame)
        self.imageButton.setObjectName(u"imageButton")

        self.gridLayout.addWidget(self.imageButton, 1, 0, 1, 1)

        self.labelButton = QPushButton(self.frame)
        self.labelButton.setObjectName(u"labelButton")

        self.gridLayout.addWidget(self.labelButton, 1, 3, 1, 1)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)
        self.cancelButton.clicked.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u5220\u9664\u95ee\u9898", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u975e\u5de5\u4f5c\u76ee\u5f55\u4e0b\u7684\u6570\u636e\u96c6\u6587\u4ef6\u65e0\u6cd5\u5220\u9664", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u6211\u4eec\u65e0\u6cd5\u786e\u5b9a\u6570\u636e\u96c6\u4e2d\u54ea\u90e8\u5206\u662f\u771f\u6b63\u7684\u6570\u636e\uff0c\u54ea\u90e8\u5206\u662f\u60a8\u7684\u6587\u4ef6\u3002\n"
"\u76f4\u63a5\u5220\u9664\u7684\u8bdd\uff0c\u60a8\u7684\u6570\u636e\u5f88\u53ef\u80fd\u88ab\u8bef\u5220\n"
"\u5982\u679c\u60a8\u8feb\u5207\u9700\u8981\u5220\u9664\uff0c\u8bf7\u70b9\u51fb\u4e0b\u65b9\u5bf9\u5e94\u6309\u94ae\u8fdb\u5165\u6587\u4ef6\u5939\u5e76\u81ea\u884c\u5220\u9664\u6587\u4ef6", None))
        self.whyButton.setText(QCoreApplication.translate("Dialog", u"\u4e3a\u4ec0\u4e48\u4e0d\u80fd\u5220\u9664\uff1f", None))
        self.cancelButton.setText(QCoreApplication.translate("Dialog", u"\u786e\u5b9a", None))
        self.imageButton.setText(QCoreApplication.translate("Dialog", u"\u6253\u5f00\u56fe\u7247\u6587\u4ef6\u5939", None))
        self.labelButton.setText(QCoreApplication.translate("Dialog", u"\u6253\u5f00\u6807\u7b7e\u6587\u4ef6\u5939", None))
    # retranslateUi


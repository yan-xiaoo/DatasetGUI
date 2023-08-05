# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'format_dataset_dialogaXUHXt.ui'
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
        Dialog.resize(400, 214)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.mergeBox = QCheckBox(self.frame)
        self.mergeBox.setObjectName(u"mergeBox")

        self.gridLayout.addWidget(self.mergeBox, 3, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.nameEdit = QLineEdit(self.frame)
        self.nameEdit.setObjectName(u"nameEdit")

        self.gridLayout.addWidget(self.nameEdit, 0, 1, 1, 1)

        self.typeButton = QRadioButton(self.frame)
        self.typeButton.setObjectName(u"typeButton")
        self.typeButton.setChecked(True)

        self.gridLayout.addWidget(self.typeButton, 2, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.okButton = QPushButton(self.frame_2)
        self.okButton.setObjectName(u"okButton")

        self.horizontalLayout.addWidget(self.okButton)

        self.cancelButton = QPushButton(self.frame_2)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(Dialog)
        self.cancelButton.clicked.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u6570\u636e\u96c6\u683c\u5f0f", None))
        self.mergeBox.setText(QCoreApplication.translate("Dialog", u"\u540c\u65f6\u8f6c\u6362", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u8f6c\u6362\u4e3a", None))
        self.typeButton.setText(QCoreApplication.translate("Dialog", u"YOLO\u683c\u5f0f\u7684\u6570\u636e\u96c6", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u65b0\u6570\u636e\u96c6\u7684\u540d\u5b57", None))
        self.okButton.setText(QCoreApplication.translate("Dialog", u"\u8f6c\u6362", None))
        self.cancelButton.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi


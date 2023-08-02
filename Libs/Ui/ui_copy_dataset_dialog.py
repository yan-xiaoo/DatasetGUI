# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'copy_dataset_dialogEWIaxE.ui'
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
        Dialog.resize(400, 321)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.nameEdit = QLineEdit(self.frame)
        self.nameEdit.setObjectName(u"nameEdit")

        self.horizontalLayout.addWidget(self.nameEdit)


        self.verticalLayout.addWidget(self.frame)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.freeRadioButton = QRadioButton(self.groupBox)
        self.freeRadioButton.setObjectName(u"freeRadioButton")

        self.gridLayout.addWidget(self.freeRadioButton, 0, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.setRadioButton = QRadioButton(self.groupBox)
        self.setRadioButton.setObjectName(u"setRadioButton")
        self.setRadioButton.setChecked(True)

        self.gridLayout.addWidget(self.setRadioButton, 3, 0, 1, 1)

        self.labelPathEdit = QLineEdit(self.groupBox)
        self.labelPathEdit.setObjectName(u"labelPathEdit")

        self.gridLayout.addWidget(self.labelPathEdit, 2, 1, 1, 1)

        self.imagePathEdit = QLineEdit(self.groupBox)
        self.imagePathEdit.setObjectName(u"imagePathEdit")

        self.gridLayout.addWidget(self.imagePathEdit, 1, 1, 1, 1)

        self.imageButton = QPushButton(self.groupBox)
        self.imageButton.setObjectName(u"imageButton")

        self.gridLayout.addWidget(self.imageButton, 1, 2, 1, 1)

        self.labelButton = QPushButton(self.groupBox)
        self.labelButton.setObjectName(u"labelButton")

        self.gridLayout.addWidget(self.labelButton, 2, 2, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.copyMergeBox = QCheckBox(Dialog)
        self.copyMergeBox.setObjectName(u"copyMergeBox")
        self.copyMergeBox.setChecked(True)

        self.verticalLayout.addWidget(self.copyMergeBox)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.okButton = QPushButton(self.frame_2)
        self.okButton.setObjectName(u"okButton")

        self.horizontalLayout_2.addWidget(self.okButton)

        self.cancelButton = QPushButton(self.frame_2)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout_2.addWidget(self.cancelButton)


        self.verticalLayout.addWidget(self.frame_2)

        QWidget.setTabOrder(self.nameEdit, self.freeRadioButton)
        QWidget.setTabOrder(self.freeRadioButton, self.imagePathEdit)
        QWidget.setTabOrder(self.imagePathEdit, self.imageButton)
        QWidget.setTabOrder(self.imageButton, self.labelPathEdit)
        QWidget.setTabOrder(self.labelPathEdit, self.labelButton)
        QWidget.setTabOrder(self.labelButton, self.setRadioButton)
        QWidget.setTabOrder(self.setRadioButton, self.okButton)
        QWidget.setTabOrder(self.okButton, self.cancelButton)

        self.retranslateUi(Dialog)
        self.cancelButton.clicked.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u590d\u5236\u6570\u636e\u96c6", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u65b0\u6570\u636e\u96c6\u7684\u540d\u5b57", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u79fb\u52a8\u5230\u54ea\u91cc\uff1f", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u6807\u7b7e\u76ee\u6807\u4f4d\u7f6e", None))
        self.freeRadioButton.setText(QCoreApplication.translate("Dialog", u"\u81ea\u5b9a\u4e49\u4f4d\u7f6e", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u56fe\u7247\u76ee\u6807\u4f4d\u7f6e", None))
        self.setRadioButton.setText(QCoreApplication.translate("Dialog", u"\u5de5\u4f5c\u76ee\u5f55\u4e0b", None))
        self.imageButton.setText(QCoreApplication.translate("Dialog", u"\u6d4f\u89c8\u2026", None))
        self.labelButton.setText(QCoreApplication.translate("Dialog", u"\u6d4f\u89c8\u2026", None))
        self.copyMergeBox.setText(QCoreApplication.translate("Dialog", u"\u540c\u65f6\u590d\u5236", None))
        self.okButton.setText(QCoreApplication.translate("Dialog", u"\u786e\u8ba4", None))
        self.cancelButton.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi


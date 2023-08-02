# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'divide_dataset_dialogPxtQHb.ui'
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
        Dialog.resize(400, 383)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.trainBox = QSpinBox(self.groupBox)
        self.trainBox.setObjectName(u"trainBox")
        self.trainBox.setMinimum(1)
        self.trainBox.setMaximum(99)
        self.trainBox.setValue(90)

        self.gridLayout.addWidget(self.trainBox, 0, 1, 1, 1)

        self.valBox = QSpinBox(self.groupBox)
        self.valBox.setObjectName(u"valBox")
        self.valBox.setMinimum(1)
        self.valBox.setMaximum(99)
        self.valBox.setValue(10)

        self.gridLayout.addWidget(self.valBox, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.trainEdit = QLineEdit(self.groupBox_2)
        self.trainEdit.setObjectName(u"trainEdit")

        self.gridLayout_2.addWidget(self.trainEdit, 0, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.valEdit = QLineEdit(self.groupBox_2)
        self.valEdit.setObjectName(u"valEdit")

        self.gridLayout_2.addWidget(self.valEdit, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.twodirButton = QRadioButton(self.groupBox_3)
        self.twodirButton.setObjectName(u"twodirButton")

        self.verticalLayout_2.addWidget(self.twodirButton)

        self.onedirButton = QRadioButton(self.groupBox_3)
        self.onedirButton.setObjectName(u"onedirButton")
        self.onedirButton.setChecked(True)

        self.verticalLayout_2.addWidget(self.onedirButton)


        self.verticalLayout.addWidget(self.groupBox_3)

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

        QWidget.setTabOrder(self.trainBox, self.valBox)
        QWidget.setTabOrder(self.valBox, self.trainEdit)
        QWidget.setTabOrder(self.trainEdit, self.valEdit)
        QWidget.setTabOrder(self.valEdit, self.twodirButton)
        QWidget.setTabOrder(self.twodirButton, self.onedirButton)
        QWidget.setTabOrder(self.onedirButton, self.okButton)
        QWidget.setTabOrder(self.okButton, self.cancelButton)

        self.retranslateUi(Dialog)
        self.cancelButton.clicked.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u5206\u5272\u6570\u636e\u96c6", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u5206\u5272\u6bd4\u4f8b", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u8bad\u7ec3\u96c6\u6bd4\u4f8b", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u9a8c\u8bc1\u96c6\u6bd4\u4f8b", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u4e24\u8005\u6bd4\u4f8b\u4e4b\u548c\u5fc5\u987b\u4e3a100", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"\u65b0\u6570\u636e\u96c6\u540d\u79f0", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u8bad\u7ec3\u96c6\u540d\u79f0", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u9a8c\u8bc1\u96c6\u540d\u79f0", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0\u65b9\u5f0f", None))
        self.twodirButton.setText(QCoreApplication.translate("Dialog", u"\u5206\u522b\u653e\u5728\u4e24\u4e2a\u76ee\u5f55\u4e0b", None))
        self.onedirButton.setText(QCoreApplication.translate("Dialog", u"\u6309\u7167\u6570\u636e\u96c6\u6807\u51c6\u683c\u5f0f\uff0c\u5b58\u653e\u5728\u540c\u4e00\u76ee\u5f55\u4e0b", None))
        self.okButton.setText(QCoreApplication.translate("Dialog", u"\u786e\u8ba4", None))
        self.cancelButton.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi


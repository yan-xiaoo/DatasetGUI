# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_dataset_dialogJQQcBU.ui'
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
        Dialog.resize(400, 524)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.datasetTypeBox = QComboBox(self.groupBox)
        self.datasetTypeBox.addItem("")
        self.datasetTypeBox.addItem("")
        self.datasetTypeBox.setObjectName(u"datasetTypeBox")

        self.horizontalLayout.addWidget(self.datasetTypeBox)


        self.verticalLayout.addWidget(self.groupBox)

        self.cocoBox = QGroupBox(Dialog)
        self.cocoBox.setObjectName(u"cocoBox")
        self.gridLayout = QGridLayout(self.cocoBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cocoLabelEdit = QLineEdit(self.cocoBox)
        self.cocoLabelEdit.setObjectName(u"cocoLabelEdit")

        self.gridLayout.addWidget(self.cocoLabelEdit, 2, 1, 1, 1)

        self.cocoImageEdit = QLineEdit(self.cocoBox)
        self.cocoImageEdit.setObjectName(u"cocoImageEdit")

        self.gridLayout.addWidget(self.cocoImageEdit, 1, 1, 1, 1)

        self.label = QLabel(self.cocoBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.cocoBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_2 = QLabel(self.cocoBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.cocoImageButton = QPushButton(self.cocoBox)
        self.cocoImageButton.setObjectName(u"cocoImageButton")

        self.gridLayout.addWidget(self.cocoImageButton, 1, 2, 1, 1)

        self.cocoLabelButton = QPushButton(self.cocoBox)
        self.cocoLabelButton.setObjectName(u"cocoLabelButton")

        self.gridLayout.addWidget(self.cocoLabelButton, 2, 2, 1, 1)

        self.cocoName = QLineEdit(self.cocoBox)
        self.cocoName.setObjectName(u"cocoName")

        self.gridLayout.addWidget(self.cocoName, 0, 1, 1, 2)


        self.verticalLayout.addWidget(self.cocoBox)

        self.yoloBox = QGroupBox(Dialog)
        self.yoloBox.setObjectName(u"yoloBox")
        self.gridLayout_2 = QGridLayout(self.yoloBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.yoloLabelEdit = QLineEdit(self.yoloBox)
        self.yoloLabelEdit.setObjectName(u"yoloLabelEdit")

        self.gridLayout_2.addWidget(self.yoloLabelEdit, 2, 1, 1, 1)

        self.yoloImageEdit = QLineEdit(self.yoloBox)
        self.yoloImageEdit.setObjectName(u"yoloImageEdit")

        self.gridLayout_2.addWidget(self.yoloImageEdit, 1, 1, 1, 1)

        self.label_4 = QLabel(self.yoloBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.yoloBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_6 = QLabel(self.yoloBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)

        self.yoloImageButton = QPushButton(self.yoloBox)
        self.yoloImageButton.setObjectName(u"yoloImageButton")

        self.gridLayout_2.addWidget(self.yoloImageButton, 1, 2, 1, 1)

        self.yoloLabelButton = QPushButton(self.yoloBox)
        self.yoloLabelButton.setObjectName(u"yoloLabelButton")

        self.gridLayout_2.addWidget(self.yoloLabelButton, 2, 2, 1, 1)

        self.yoloName = QLineEdit(self.yoloBox)
        self.yoloName.setObjectName(u"yoloName")

        self.gridLayout_2.addWidget(self.yoloName, 0, 1, 1, 2)


        self.verticalLayout.addWidget(self.yoloBox)

        self.groupBox_4 = QGroupBox(Dialog)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkDatasetBox = QCheckBox(self.groupBox_4)
        self.checkDatasetBox.setObjectName(u"checkDatasetBox")
        self.checkDatasetBox.setChecked(True)

        self.verticalLayout_2.addWidget(self.checkDatasetBox)

        self.cleanDatasetBox = QCheckBox(self.groupBox_4)
        self.cleanDatasetBox.setObjectName(u"cleanDatasetBox")
        self.cleanDatasetBox.setChecked(False)

        self.verticalLayout_2.addWidget(self.cleanDatasetBox)

        self.copyDatasetBox = QCheckBox(self.groupBox_4)
        self.copyDatasetBox.setObjectName(u"copyDatasetBox")
        self.copyDatasetBox.setChecked(True)

        self.verticalLayout_2.addWidget(self.copyDatasetBox)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.okButton = QPushButton(self.frame)
        self.okButton.setObjectName(u"okButton")

        self.horizontalLayout_2.addWidget(self.okButton)

        self.cancelButton = QPushButton(self.frame)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout_2.addWidget(self.cancelButton)


        self.verticalLayout.addWidget(self.frame)

        QWidget.setTabOrder(self.datasetTypeBox, self.cocoName)
        QWidget.setTabOrder(self.cocoName, self.cocoImageEdit)
        QWidget.setTabOrder(self.cocoImageEdit, self.cocoImageButton)
        QWidget.setTabOrder(self.cocoImageButton, self.cocoLabelEdit)
        QWidget.setTabOrder(self.cocoLabelEdit, self.cocoLabelButton)
        QWidget.setTabOrder(self.cocoLabelButton, self.yoloName)
        QWidget.setTabOrder(self.yoloName, self.yoloImageEdit)
        QWidget.setTabOrder(self.yoloImageEdit, self.yoloImageButton)
        QWidget.setTabOrder(self.yoloImageButton, self.yoloLabelEdit)
        QWidget.setTabOrder(self.yoloLabelEdit, self.yoloLabelButton)
        QWidget.setTabOrder(self.yoloLabelButton, self.checkDatasetBox)
        QWidget.setTabOrder(self.checkDatasetBox, self.cleanDatasetBox)
        QWidget.setTabOrder(self.cleanDatasetBox, self.copyDatasetBox)
        QWidget.setTabOrder(self.copyDatasetBox, self.okButton)
        QWidget.setTabOrder(self.okButton, self.cancelButton)

        self.retranslateUi(Dialog)
        self.cancelButton.clicked.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0\u6570\u636e\u96c6", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u6570\u636e\u96c6\u7c7b\u578b", None))
        self.datasetTypeBox.setItemText(0, QCoreApplication.translate("Dialog", u"COCO\u6570\u636e\u96c6", None))
        self.datasetTypeBox.setItemText(1, QCoreApplication.translate("Dialog", u"YOLO\u6570\u636e\u96c6", None))

        self.cocoBox.setTitle(QCoreApplication.translate("Dialog", u"\u6570\u636e\u96c6\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u540d\u79f0", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u56fe\u7247\u6587\u4ef6\u5939", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"COCO\u6570\u636e\u96c6", None))
        self.cocoImageButton.setText(QCoreApplication.translate("Dialog", u"\u6d4f\u89c8\u2026", None))
        self.cocoLabelButton.setText(QCoreApplication.translate("Dialog", u"\u6d4f\u89c8\u2026", None))
        self.yoloBox.setTitle(QCoreApplication.translate("Dialog", u"\u6570\u636e\u96c6\u4fe1\u606f", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u540d\u79f0", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u56fe\u7247\u6587\u4ef6\u5939", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u6807\u7b7e\u6587\u4ef6\u5939", None))
        self.yoloImageButton.setText(QCoreApplication.translate("Dialog", u"\u6d4f\u89c8\u2026", None))
        self.yoloLabelButton.setText(QCoreApplication.translate("Dialog", u"\u6d4f\u89c8\u2026", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"\u9009\u9879", None))
        self.checkDatasetBox.setText(QCoreApplication.translate("Dialog", u"\u5bfc\u5165\u65f6\u68c0\u67e5\u6570\u636e\u96c6", None))
        self.cleanDatasetBox.setText(QCoreApplication.translate("Dialog", u"\u5bfc\u5165\u65f6\u6e05\u7406\u6570\u636e\u96c6", None))
        self.copyDatasetBox.setText(QCoreApplication.translate("Dialog", u"\u62f7\u8d1d\u6570\u636e\u96c6\u81f3\u5de5\u4f5c\u76ee\u5f55\u4e0b", None))
        self.okButton.setText(QCoreApplication.translate("Dialog", u"\u786e\u8ba4", None))
        self.cancelButton.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi


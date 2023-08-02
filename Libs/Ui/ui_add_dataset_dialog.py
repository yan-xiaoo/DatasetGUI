# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_dataset_dialogwPLySi.ui'
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
        Dialog.resize(400, 1261)
        Dialog.setAutoFillBackground(True)
        Dialog.setSizeGripEnabled(True)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.datasetTypeBox = QComboBox(self.groupBox)
        self.datasetTypeBox.addItem("")
        self.datasetTypeBox.addItem("")
        self.datasetTypeBox.setObjectName(u"datasetTypeBox")

        self.verticalLayout_3.addWidget(self.datasetTypeBox)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.label_7)

        self.singleButton = QRadioButton(self.groupBox)
        self.singleButton.setObjectName(u"singleButton")
        self.singleButton.setChecked(True)

        self.verticalLayout_3.addWidget(self.singleButton)

        self.multipleButton = QRadioButton(self.groupBox)
        self.multipleButton.setObjectName(u"multipleButton")

        self.verticalLayout_3.addWidget(self.multipleButton)


        self.verticalLayout.addWidget(self.groupBox)

        self.cocoBox = QGroupBox(Dialog)
        self.cocoBox.setObjectName(u"cocoBox")
        self.gridLayout = QGridLayout(self.cocoBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.label_2 = QLabel(self.cocoBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label = QLabel(self.cocoBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.cocoBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.cocoName = QLineEdit(self.cocoBox)
        self.cocoName.setObjectName(u"cocoName")

        self.gridLayout.addWidget(self.cocoName, 0, 1, 1, 2)

        self.cocoImageEdit = QLineEdit(self.cocoBox)
        self.cocoImageEdit.setObjectName(u"cocoImageEdit")

        self.gridLayout.addWidget(self.cocoImageEdit, 1, 1, 1, 1)

        self.cocoLabelButton = QPushButton(self.cocoBox)
        self.cocoLabelButton.setObjectName(u"cocoLabelButton")

        self.gridLayout.addWidget(self.cocoLabelButton, 2, 2, 1, 1)

        self.cocoLabelEdit = QLineEdit(self.cocoBox)
        self.cocoLabelEdit.setObjectName(u"cocoLabelEdit")

        self.gridLayout.addWidget(self.cocoLabelEdit, 2, 1, 1, 1)

        self.cocoImageButton = QPushButton(self.cocoBox)
        self.cocoImageButton.setObjectName(u"cocoImageButton")

        self.gridLayout.addWidget(self.cocoImageButton, 1, 2, 1, 1)


        self.verticalLayout.addWidget(self.cocoBox)

        self.cocoMergeFrame = QFrame(Dialog)
        self.cocoMergeFrame.setObjectName(u"cocoMergeFrame")
        self.cocoMergeFrame.setFrameShape(QFrame.NoFrame)
        self.cocoMergeFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.cocoMergeFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, -1)
        self.frame_4 = QFrame(self.cocoMergeFrame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalLayout.setContentsMargins(-1, 0, 0, 0)
        self.label_14 = QLabel(self.frame_4)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout.addWidget(self.label_14)

        self.cocoMergeEdit = QLineEdit(self.frame_4)
        self.cocoMergeEdit.setObjectName(u"cocoMergeEdit")

        self.horizontalLayout.addWidget(self.cocoMergeEdit)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.groupBox_5 = QGroupBox(self.cocoMergeFrame)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setEnabled(True)
        self.gridLayout_5 = QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.label_11 = QLabel(self.groupBox_5)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 0, 0, 1, 1)

        self.cocoTrainEdit = QLineEdit(self.groupBox_5)
        self.cocoTrainEdit.setObjectName(u"cocoTrainEdit")

        self.gridLayout_5.addWidget(self.cocoTrainEdit, 0, 1, 1, 2)

        self.label_13 = QLabel(self.groupBox_5)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_5.addWidget(self.label_13, 1, 0, 1, 1)

        self.cocoTrainImageEdit = QLineEdit(self.groupBox_5)
        self.cocoTrainImageEdit.setObjectName(u"cocoTrainImageEdit")

        self.gridLayout_5.addWidget(self.cocoTrainImageEdit, 1, 1, 1, 1)

        self.cocoTrainImageButton = QPushButton(self.groupBox_5)
        self.cocoTrainImageButton.setObjectName(u"cocoTrainImageButton")

        self.gridLayout_5.addWidget(self.cocoTrainImageButton, 1, 2, 1, 1)

        self.label_12 = QLabel(self.groupBox_5)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_5.addWidget(self.label_12, 2, 0, 1, 1)

        self.cocoTrainLabelEdit = QLineEdit(self.groupBox_5)
        self.cocoTrainLabelEdit.setObjectName(u"cocoTrainLabelEdit")

        self.gridLayout_5.addWidget(self.cocoTrainLabelEdit, 2, 1, 1, 1)

        self.cocoTrainLabelButton = QPushButton(self.groupBox_5)
        self.cocoTrainLabelButton.setObjectName(u"cocoTrainLabelButton")

        self.gridLayout_5.addWidget(self.cocoTrainLabelButton, 2, 2, 1, 1)


        self.verticalLayout_5.addWidget(self.groupBox_5)

        self.groupBox_3 = QGroupBox(self.cocoMergeFrame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.cocoValLabelButton = QPushButton(self.groupBox_3)
        self.cocoValLabelButton.setObjectName(u"cocoValLabelButton")

        self.gridLayout_4.addWidget(self.cocoValLabelButton, 3, 2, 1, 1)

        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_4.addWidget(self.label_8, 1, 0, 1, 1)

        self.cocoValEdit = QLineEdit(self.groupBox_3)
        self.cocoValEdit.setObjectName(u"cocoValEdit")

        self.gridLayout_4.addWidget(self.cocoValEdit, 1, 1, 1, 2)

        self.cocoValImageEdit = QLineEdit(self.groupBox_3)
        self.cocoValImageEdit.setObjectName(u"cocoValImageEdit")

        self.gridLayout_4.addWidget(self.cocoValImageEdit, 2, 1, 1, 1)

        self.cocoValImageButton = QPushButton(self.groupBox_3)
        self.cocoValImageButton.setObjectName(u"cocoValImageButton")

        self.gridLayout_4.addWidget(self.cocoValImageButton, 2, 2, 1, 1)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 3, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 2, 0, 1, 1)

        self.cocoValLabelEdit = QLineEdit(self.groupBox_3)
        self.cocoValLabelEdit.setObjectName(u"cocoValLabelEdit")

        self.gridLayout_4.addWidget(self.cocoValLabelEdit, 3, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.groupBox_3)


        self.verticalLayout.addWidget(self.cocoMergeFrame)

        self.yoloBox = QGroupBox(Dialog)
        self.yoloBox.setObjectName(u"yoloBox")
        self.gridLayout_2 = QGridLayout(self.yoloBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.label_5 = QLabel(self.yoloBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)

        self.yoloLabelEdit = QLineEdit(self.yoloBox)
        self.yoloLabelEdit.setObjectName(u"yoloLabelEdit")

        self.gridLayout_2.addWidget(self.yoloLabelEdit, 3, 1, 1, 1)

        self.yoloImageEdit = QLineEdit(self.yoloBox)
        self.yoloImageEdit.setObjectName(u"yoloImageEdit")

        self.gridLayout_2.addWidget(self.yoloImageEdit, 2, 1, 1, 1)

        self.label_4 = QLabel(self.yoloBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.yoloImageButton = QPushButton(self.yoloBox)
        self.yoloImageButton.setObjectName(u"yoloImageButton")

        self.gridLayout_2.addWidget(self.yoloImageButton, 2, 2, 1, 1)

        self.yoloLabelButton = QPushButton(self.yoloBox)
        self.yoloLabelButton.setObjectName(u"yoloLabelButton")

        self.gridLayout_2.addWidget(self.yoloLabelButton, 3, 2, 1, 1)

        self.label_6 = QLabel(self.yoloBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)

        self.yoloName = QLineEdit(self.yoloBox)
        self.yoloName.setObjectName(u"yoloName")
        self.yoloName.setAutoFillBackground(False)

        self.gridLayout_2.addWidget(self.yoloName, 1, 1, 1, 2)


        self.verticalLayout.addWidget(self.yoloBox)

        self.yoloMergeFrame = QFrame(Dialog)
        self.yoloMergeFrame.setObjectName(u"yoloMergeFrame")
        self.yoloMergeFrame.setFrameShape(QFrame.NoFrame)
        self.yoloMergeFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.yoloMergeFrame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 12)
        self.frame_6 = QFrame(self.yoloMergeFrame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 12)
        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_3.addWidget(self.label_15)

        self.yoloMergeEdit = QLineEdit(self.frame_6)
        self.yoloMergeEdit.setObjectName(u"yoloMergeEdit")

        self.horizontalLayout_3.addWidget(self.yoloMergeEdit)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.groupBox_6 = QGroupBox(self.yoloMergeFrame)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setEnabled(True)
        self.gridLayout_6 = QGridLayout(self.groupBox_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.label_16 = QLabel(self.groupBox_6)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_6.addWidget(self.label_16, 0, 0, 1, 1)

        self.yoloTrainEdit = QLineEdit(self.groupBox_6)
        self.yoloTrainEdit.setObjectName(u"yoloTrainEdit")

        self.gridLayout_6.addWidget(self.yoloTrainEdit, 0, 1, 1, 2)

        self.label_17 = QLabel(self.groupBox_6)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_6.addWidget(self.label_17, 1, 0, 1, 1)

        self.yoloTrainImageEdit = QLineEdit(self.groupBox_6)
        self.yoloTrainImageEdit.setObjectName(u"yoloTrainImageEdit")

        self.gridLayout_6.addWidget(self.yoloTrainImageEdit, 1, 1, 1, 1)

        self.yoloTrainImageButton = QPushButton(self.groupBox_6)
        self.yoloTrainImageButton.setObjectName(u"yoloTrainImageButton")

        self.gridLayout_6.addWidget(self.yoloTrainImageButton, 1, 2, 1, 1)

        self.label_18 = QLabel(self.groupBox_6)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_6.addWidget(self.label_18, 2, 0, 1, 1)

        self.yoloTrainLabelEdit = QLineEdit(self.groupBox_6)
        self.yoloTrainLabelEdit.setObjectName(u"yoloTrainLabelEdit")

        self.gridLayout_6.addWidget(self.yoloTrainLabelEdit, 2, 1, 1, 1)

        self.yoloTrainLabelButton = QPushButton(self.groupBox_6)
        self.yoloTrainLabelButton.setObjectName(u"yoloTrainLabelButton")

        self.gridLayout_6.addWidget(self.yoloTrainLabelButton, 2, 2, 1, 1)


        self.verticalLayout_6.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.yoloMergeFrame)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_7 = QGridLayout(self.groupBox_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.yoloValLabelButton = QPushButton(self.groupBox_7)
        self.yoloValLabelButton.setObjectName(u"yoloValLabelButton")

        self.gridLayout_7.addWidget(self.yoloValLabelButton, 3, 2, 1, 1)

        self.label_19 = QLabel(self.groupBox_7)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_7.addWidget(self.label_19, 1, 0, 1, 1)

        self.yoloValEdit = QLineEdit(self.groupBox_7)
        self.yoloValEdit.setObjectName(u"yoloValEdit")

        self.gridLayout_7.addWidget(self.yoloValEdit, 1, 1, 1, 2)

        self.yoloValImageEdit = QLineEdit(self.groupBox_7)
        self.yoloValImageEdit.setObjectName(u"yoloValImageEdit")

        self.gridLayout_7.addWidget(self.yoloValImageEdit, 2, 1, 1, 1)

        self.yoloValImageButton = QPushButton(self.groupBox_7)
        self.yoloValImageButton.setObjectName(u"yoloValImageButton")

        self.gridLayout_7.addWidget(self.yoloValImageButton, 2, 2, 1, 1)

        self.label_20 = QLabel(self.groupBox_7)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_7.addWidget(self.label_20, 3, 0, 1, 1)

        self.label_21 = QLabel(self.groupBox_7)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_7.addWidget(self.label_21, 2, 0, 1, 1)

        self.yoloValLabelEdit = QLineEdit(self.groupBox_7)
        self.yoloValLabelEdit.setObjectName(u"yoloValLabelEdit")

        self.gridLayout_7.addWidget(self.yoloValLabelEdit, 3, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.groupBox_7)


        self.verticalLayout.addWidget(self.yoloMergeFrame)

        self.groupBox_4 = QGroupBox(Dialog)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMinAndMaxSize)
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
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMinAndMaxSize)
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

        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0\u5f62\u5f0f", None))
        self.singleButton.setText(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0\u5355\u4e2a\u6570\u636e\u96c6", None))
        self.multipleButton.setText(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0\u4e00\u5bf9\u8bad\u7ec3\u96c6\u4e0e\u9a8c\u8bc1\u96c6", None))
        self.cocoBox.setTitle(QCoreApplication.translate("Dialog", u"\u6570\u636e\u96c6\u4fe1\u606f", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"COCO\u6570\u636e\u96c6", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u540d\u79f0", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u56fe\u7247\u6587\u4ef6\u5939", None))
        self.cocoLabelButton.setText(QCoreApplication.translate("Dialog", u"\u6d4f\u89c8\u2026", None))
        self.cocoImageButton.setText(QCoreApplication.translate("Dialog", u"\u6d4f\u89c8\u2026", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"\u540d\u79f0", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Dialog", u"\u8bad\u7ec3\u96c6\u4fe1\u606f", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u8bad\u7ec3\u96c6\u540d\u79f0", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"\u56fe\u7247\u6587\u4ef6\u5939", None))
        self.cocoTrainImageButton.setText(QCoreApplication.translate("Dialog", u"\u6d4f\u89c8\u2026", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"COCO\u6570\u636e\u96c6", None))
        self.cocoTrainLabelButton.setText(QCoreApplication.translate("Dialog", u"\u6d4f\u89c8\u2026", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"\u9a8c\u8bc1\u96c6\u4fe1\u606f", None))
        self.cocoValLabelButton.setText(QCoreApplication.translate("Dialog", u"\u6d4f\u89c8\u2026", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u9a8c\u8bc1\u96c6\u540d\u79f0", None))
        self.cocoValImageButton.setText(QCoreApplication.translate("Dialog", u"\u6d4f\u89c8\u2026", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"COCO\u6570\u636e\u96c6", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u56fe\u7247\u6587\u4ef6\u5939", None))
        self.yoloBox.setTitle(QCoreApplication.translate("Dialog", u"\u6570\u636e\u96c6\u4fe1\u606f", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u56fe\u7247\u6587\u4ef6\u5939", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u540d\u79f0", None))
        self.yoloImageButton.setText(QCoreApplication.translate("Dialog", u"\u6d4f\u89c8\u2026", None))
        self.yoloLabelButton.setText(QCoreApplication.translate("Dialog", u"\u6d4f\u89c8\u2026", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u6807\u7b7e\u6587\u4ef6\u5939", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"\u540d\u79f0", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Dialog", u"\u8bad\u7ec3\u96c6\u4fe1\u606f", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"\u8bad\u7ec3\u96c6\u540d\u79f0", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"\u56fe\u7247\u6587\u4ef6\u5939", None))
        self.yoloTrainImageButton.setText(QCoreApplication.translate("Dialog", u"\u6d4f\u89c8\u2026", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"\u6807\u7b7e\u6587\u4ef6\u5939", None))
        self.yoloTrainLabelButton.setText(QCoreApplication.translate("Dialog", u"\u6d4f\u89c8\u2026", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Dialog", u"\u9a8c\u8bc1\u96c6\u4fe1\u606f", None))
        self.yoloValLabelButton.setText(QCoreApplication.translate("Dialog", u"\u6d4f\u89c8\u2026", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"\u9a8c\u8bc1\u96c6\u540d\u79f0", None))
        self.yoloValImageButton.setText(QCoreApplication.translate("Dialog", u"\u6d4f\u89c8\u2026", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", u"\u6807\u7b7e\u6587\u4ef6\u5939", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"\u56fe\u7247\u6587\u4ef6\u5939", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"\u9009\u9879", None))
        self.checkDatasetBox.setText(QCoreApplication.translate("Dialog", u"\u5bfc\u5165\u65f6\u68c0\u67e5\u6570\u636e\u96c6", None))
        self.cleanDatasetBox.setText(QCoreApplication.translate("Dialog", u"\u5bfc\u5165\u65f6\u6e05\u7406\u6570\u636e\u96c6", None))
        self.copyDatasetBox.setText(QCoreApplication.translate("Dialog", u"\u62f7\u8d1d\u6570\u636e\u96c6\u81f3\u5de5\u4f5c\u76ee\u5f55\u4e0b", None))
        self.okButton.setText(QCoreApplication.translate("Dialog", u"\u786e\u8ba4", None))
        self.cancelButton.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi


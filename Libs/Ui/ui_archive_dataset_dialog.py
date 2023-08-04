# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'archive_dataset_dialogdhRBVx.ui'
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
        Dialog.resize(448, 336)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.outputEdit = QLineEdit(self.frame)
        self.outputEdit.setObjectName(u"outputEdit")

        self.gridLayout.addWidget(self.outputEdit, 1, 1, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.outputButton = QPushButton(self.frame)
        self.outputButton.setObjectName(u"outputButton")

        self.gridLayout.addWidget(self.outputButton, 1, 2, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.nameEdit = QLineEdit(self.frame)
        self.nameEdit.setObjectName(u"nameEdit")

        self.gridLayout.addWidget(self.nameEdit, 0, 1, 1, 2)


        self.verticalLayout.addWidget(self.frame)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.zipButton = QRadioButton(self.groupBox)
        self.zipButton.setObjectName(u"zipButton")

        self.verticalLayout_2.addWidget(self.zipButton)

        self.tarButton = QRadioButton(self.groupBox)
        self.tarButton.setObjectName(u"tarButton")
        self.tarButton.setChecked(True)

        self.verticalLayout_2.addWidget(self.tarButton)


        self.verticalLayout.addWidget(self.groupBox)

        self.ignoreBox = QCheckBox(Dialog)
        self.ignoreBox.setObjectName(u"ignoreBox")
        self.ignoreBox.setChecked(True)

        self.verticalLayout.addWidget(self.ignoreBox)

        self.archiveMergeBox = QCheckBox(Dialog)
        self.archiveMergeBox.setObjectName(u"archiveMergeBox")

        self.verticalLayout.addWidget(self.archiveMergeBox)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

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

        QWidget.setTabOrder(self.nameEdit, self.outputEdit)
        QWidget.setTabOrder(self.outputEdit, self.outputButton)
        QWidget.setTabOrder(self.outputButton, self.zipButton)
        QWidget.setTabOrder(self.zipButton, self.tarButton)
        QWidget.setTabOrder(self.tarButton, self.ignoreBox)
        QWidget.setTabOrder(self.ignoreBox, self.okButton)
        QWidget.setTabOrder(self.okButton, self.cancelButton)

        self.retranslateUi(Dialog)
        self.cancelButton.clicked.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u538b\u7f29\u6570\u636e\u96c6", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u5bfc\u51fa\u6587\u4ef6\u5939\u4f4d\u7f6e", None))
        self.outputButton.setText(QCoreApplication.translate("Dialog", u"\u6d4f\u89c8\u2026", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u5bfc\u51fa\u6587\u4ef6\u540d", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u5bfc\u51fa\u9009\u9879", None))
        self.zipButton.setText(QCoreApplication.translate("Dialog", u"ZIP\u683c\u5f0f", None))
        self.tarButton.setText(QCoreApplication.translate("Dialog", u"TAR.GZ\u683c\u5f0f", None))
#if QT_CONFIG(tooltip)
        self.ignoreBox.setToolTip(QCoreApplication.translate("Dialog", u"\u8be5\u9009\u9879\u5728macOS\u5916\u7684\u7cfb\u7edf\u4e0a\u6ca1\u6709\u4f5c\u7528", None))
#endif // QT_CONFIG(tooltip)
        self.ignoreBox.setText(QCoreApplication.translate("Dialog", u"\u5ffd\u7565.DS_Store\u6587\u4ef6", None))
        self.archiveMergeBox.setText(QCoreApplication.translate("Dialog", u"\u540c\u65f6\u538b\u7f29", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u6570\u636e\u96c6\u8f83\u5927\u65f6\uff0c\u538b\u7f29\u901f\u5ea6\u6162\u4e3a\u6b63\u5e38\u73b0\u8c61\n"
"\u672c\u7a0b\u5e8f\u7684\u538b\u7f29\u901f\u5ea6\u5927\u6982\u548c\u64cd\u4f5c\u7cfb\u7edf\u81ea\u5e26\u5de5\u5177\u4e00\u6837", None))
        self.okButton.setText(QCoreApplication.translate("Dialog", u"\u786e\u8ba4", None))
        self.cancelButton.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi


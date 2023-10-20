# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clean_dataset_dialogdEmdTg.ui'
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
        Dialog.resize(398, 246)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelCheckBox = QCheckBox(self.groupBox)
        self.labelCheckBox.setObjectName(u"labelCheckBox")
        self.labelCheckBox.setChecked(True)

        self.verticalLayout_2.addWidget(self.labelCheckBox)

        self.imageCheckBox = QCheckBox(self.groupBox)
        self.imageCheckBox.setObjectName(u"imageCheckBox")
        self.imageCheckBox.setChecked(True)

        self.verticalLayout_2.addWidget(self.imageCheckBox)

        self.fileCheckBox = QCheckBox(self.groupBox)
        self.fileCheckBox.setObjectName(u"fileCheckBox")
        self.fileCheckBox.setChecked(True)

        self.verticalLayout_2.addWidget(self.fileCheckBox)

        self.pointCheckBox = QCheckBox(self.groupBox)
        self.pointCheckBox.setObjectName(u"pointCheckBox")
        self.pointCheckBox.setChecked(False)

        self.verticalLayout_2.addWidget(self.pointCheckBox)


        self.verticalLayout.addWidget(self.groupBox)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

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
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u68c0\u67e5\u6570\u636e\u96c6", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u6267\u884c\u54ea\u4e9b\u68c0\u67e5\uff1f", None))
#if QT_CONFIG(tooltip)
        self.labelCheckBox.setToolTip(QCoreApplication.translate("Dialog", u"\u68c0\u67e5\u6ca1\u6709\u6807\u6ce8\u7684\u56fe\u7247\u548c\u6ca1\u6709\u4efb\u4f55\u6807\u7b7e\u7684\u7c7b\u522b", None))
#endif // QT_CONFIG(tooltip)
        self.labelCheckBox.setText(QCoreApplication.translate("Dialog", u"\u68c0\u67e5\u5197\u4f59\u6807\u6ce8", None))
#if QT_CONFIG(tooltip)
        self.imageCheckBox.setToolTip(QCoreApplication.translate("Dialog", u"\u68c0\u67e5\u62e5\u6709\u6807\u7b7e\u7684\u56fe\u7247\u662f\u5426\u5b58\u5728", None))
#endif // QT_CONFIG(tooltip)
        self.imageCheckBox.setText(QCoreApplication.translate("Dialog", u"\u68c0\u67e5\u88ab\u6807\u6ce8\u56fe\u7247\u662f\u5426\u5b58\u5728", None))
#if QT_CONFIG(tooltip)
        self.fileCheckBox.setToolTip(QCoreApplication.translate("Dialog", u"\u68c0\u67e5\u6570\u636e\u96c6\u6587\u4ef6\u5939\u5185\u662f\u5426\u6709\u56fe\u7247\u548c\u6807\u7b7e\u5916\u7684\u5176\u4ed6\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.fileCheckBox.setText(QCoreApplication.translate("Dialog", u"\u68c0\u67e5\u6570\u636e\u96c6\u5185\u662f\u5426\u6709\u5176\u4ed6\u6587\u4ef6", None))
#if QT_CONFIG(tooltip)
        self.pointCheckBox.setToolTip(QCoreApplication.translate("Dialog", u"\u68c0\u67e5\u6570\u636e\u96c6\u7684\u6bcf\u4e2a\u5206\u7c7b\u7684\u5173\u952e\u70b9\u6570\u91cf\u662f\u5426\u6b63\u786e", None))
#endif // QT_CONFIG(tooltip)
        self.pointCheckBox.setText(QCoreApplication.translate("Dialog", u"\u68c0\u67e5\u5404\u5206\u7c7b\u5173\u952e\u70b9\u7684\u4e2a\u6570", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u5728\u68c0\u67e5\u975e\u5e38\u975e\u5e38\u5927\u7684\u6570\u636e\u96c6\u65f6\uff0c\n"
"\u7a0b\u5e8f\u53ef\u80fd\u5728\u77ed\u65f6\u95f4\u5185\u65e0\u54cd\u5e94\u3002\u8fd9\u662f\u6b63\u5e38\u73b0\u8c61", None))
        self.okButton.setText(QCoreApplication.translate("Dialog", u"\u68c0\u67e5", None))
        self.cancelButton.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi


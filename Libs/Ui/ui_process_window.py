# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'process_windowbSgAGC.ui'
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
        Dialog.resize(400, 126)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Text = QLabel(Dialog)
        self.Text.setObjectName(u"Text")
        font = QFont()
        font.setPointSize(17)
        self.Text.setFont(font)

        self.verticalLayout.addWidget(self.Text)

        self.detailedText = QLabel(Dialog)
        self.detailedText.setObjectName(u"detailedText")

        self.verticalLayout.addWidget(self.detailedText)

        self.progressBar = QProgressBar(Dialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)

        self.stopButton = QPushButton(Dialog)
        self.stopButton.setObjectName(u"stopButton")

        self.verticalLayout.addWidget(self.stopButton)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u8fdb\u5ea6\u7a97\u53e3", None))
        self.Text.setText(QCoreApplication.translate("Dialog", u"\u4efb\u52a1", None))
        self.detailedText.setText(QCoreApplication.translate("Dialog", u"\u8be6\u7ec6\u63cf\u8ff0", None))
        self.stopButton.setText(QCoreApplication.translate("Dialog", u"\u505c\u6b62", None))
    # retranslateUi


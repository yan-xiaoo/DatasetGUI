# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dataset_windowWEnOHG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(700, 500)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.browseLabelPath = QPushButton(self.groupBox)
        self.browseLabelPath.setObjectName(u"browseLabelPath")

        self.gridLayout.addWidget(self.browseLabelPath, 2, 2, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.browseImagePath = QPushButton(self.groupBox)
        self.browseImagePath.setObjectName(u"browseImagePath")

        self.gridLayout.addWidget(self.browseImagePath, 1, 2, 1, 1)

        self.imagePathEdit = QLineEdit(self.groupBox)
        self.imagePathEdit.setObjectName(u"imagePathEdit")

        self.gridLayout.addWidget(self.imagePathEdit, 1, 1, 1, 1)

        self.labelPathEdit = QLineEdit(self.groupBox)
        self.labelPathEdit.setObjectName(u"labelPathEdit")

        self.gridLayout.addWidget(self.labelPathEdit, 2, 1, 1, 1)

        self.showImagePathButton = QPushButton(self.groupBox)
        self.showImagePathButton.setObjectName(u"showImagePathButton")

        self.gridLayout.addWidget(self.showImagePathButton, 1, 3, 1, 1)

        self.nameEdit = QLineEdit(self.groupBox)
        self.nameEdit.setObjectName(u"nameEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameEdit.sizePolicy().hasHeightForWidth())
        self.nameEdit.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.nameEdit, 0, 1, 1, 3)

        self.update_info = QPushButton(self.groupBox)
        self.update_info.setObjectName(u"update_info")

        self.gridLayout.addWidget(self.update_info, 3, 3, 1, 1)

        self.showLabelPathButton = QPushButton(self.groupBox)
        self.showLabelPathButton.setObjectName(u"showLabelPathButton")

        self.gridLayout.addWidget(self.showLabelPathButton, 2, 3, 1, 1)

        self.dataTypeLabel = QLabel(self.groupBox)
        self.dataTypeLabel.setObjectName(u"dataTypeLabel")
        self.dataTypeLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.dataTypeLabel, 3, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_5 = QPushButton(self.groupBox_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setCheckable(False)

        self.gridLayout_2.addWidget(self.pushButton_5, 0, 0, 1, 1)

        self.copyDatasetButton = QPushButton(self.groupBox_2)
        self.copyDatasetButton.setObjectName(u"copyDatasetButton")
        self.copyDatasetButton.setEnabled(False)

        self.gridLayout_2.addWidget(self.copyDatasetButton, 0, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.groupBox_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setEnabled(False)

        self.gridLayout_2.addWidget(self.pushButton_7, 0, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.groupBox_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setEnabled(False)

        self.gridLayout_2.addWidget(self.pushButton_8, 1, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.groupBox_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setEnabled(False)

        self.gridLayout_2.addWidget(self.pushButton_9, 1, 2, 1, 1)

        self.deleteDatasetButton = QPushButton(self.groupBox_2)
        self.deleteDatasetButton.setObjectName(u"deleteDatasetButton")
        self.deleteDatasetButton.setEnabled(True)

        self.gridLayout_2.addWidget(self.deleteDatasetButton, 2, 1, 1, 1)

        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)

        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)

        self.cleanDatasetButton = QPushButton(self.groupBox_2)
        self.cleanDatasetButton.setObjectName(u"cleanDatasetButton")
        self.cleanDatasetButton.setEnabled(False)

        self.gridLayout_2.addWidget(self.cleanDatasetButton, 2, 2, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        QWidget.setTabOrder(self.nameEdit, self.imagePathEdit)
        QWidget.setTabOrder(self.imagePathEdit, self.browseImagePath)
        QWidget.setTabOrder(self.browseImagePath, self.showImagePathButton)
        QWidget.setTabOrder(self.showImagePathButton, self.labelPathEdit)
        QWidget.setTabOrder(self.labelPathEdit, self.browseLabelPath)
        QWidget.setTabOrder(self.browseLabelPath, self.showLabelPathButton)
        QWidget.setTabOrder(self.showLabelPathButton, self.update_info)
        QWidget.setTabOrder(self.update_info, self.pushButton_5)
        QWidget.setTabOrder(self.pushButton_5, self.copyDatasetButton)
        QWidget.setTabOrder(self.copyDatasetButton, self.pushButton_7)
        QWidget.setTabOrder(self.pushButton_7, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.pushButton_8)
        QWidget.setTabOrder(self.pushButton_8, self.pushButton_9)
        QWidget.setTabOrder(self.pushButton_9, self.deleteDatasetButton)
        QWidget.setTabOrder(self.deleteDatasetButton, self.cleanDatasetButton)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u6570\u636e\u96c6\u8be6\u60c5", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u57fa\u672c\u4fe1\u606f", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u6807\u7b7e\u4f4d\u7f6e", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u56fe\u7247\u4f4d\u7f6e", None))
        self.browseLabelPath.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8\u2026", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u540d\u79f0", None))
        self.browseImagePath.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8\u2026", None))
#if QT_CONFIG(tooltip)
        self.showImagePathButton.setToolTip(QCoreApplication.translate("Form", u"\u5982\u679c\u6ca1\u6709\u53cd\u5e94\uff0c\u8bf4\u660e\u60a8\u586b\u5199\u7684\u8def\u5f84\u4e0d\u5b58\u5728", None))
#endif // QT_CONFIG(tooltip)
        self.showImagePathButton.setText(QCoreApplication.translate("Form", u"\u5728\u7cfb\u7edf\u4e2d\u663e\u793a", None))
#if QT_CONFIG(tooltip)
        self.update_info.setToolTip(QCoreApplication.translate("Form", u"\u53ea\u6709\u70b9\u51fb\u8be5\u6309\u94ae\u540e\uff0c\u60a8\u5728\u4e0a\u65b9\u7684\u66f4\u6539\u624d\u4f1a\u751f\u6548", None))
#endif // QT_CONFIG(tooltip)
        self.update_info.setText(QCoreApplication.translate("Form", u"\u66f4\u65b0\u4fe1\u606f", None))
#if QT_CONFIG(tooltip)
        self.showLabelPathButton.setToolTip(QCoreApplication.translate("Form", u"\u5982\u679c\u6ca1\u6709\u53cd\u5e94\uff0c\u8bf4\u660e\u60a8\u586b\u5199\u7684\u8def\u5f84\u4e0d\u5b58\u5728", None))
#endif // QT_CONFIG(tooltip)
        self.showLabelPathButton.setText(QCoreApplication.translate("Form", u"\u5728\u7cfb\u7edf\u4e2d\u663e\u793a", None))
        self.dataTypeLabel.setText("")
#if QT_CONFIG(tooltip)
        self.groupBox_2.setToolTip(QCoreApplication.translate("Form", u"\u65e0\u6cd5\u70b9\u51fb\u7684\u6309\u94ae\u5c31\u662f\u8fd8\u6ca1\u505a\u7684\uff08\uff09", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u64cd\u4f5c", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u6807\u6ce8\u2026", None))
        self.copyDatasetButton.setText(QCoreApplication.translate("Form", u"\u590d\u5236\u2026", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"\u5408\u5e76\u2026", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"\u5212\u5206\u4e3a\u8bad\u7ec3\u4e0e\u9a8c\u8bc1\u2026", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"\u8f6c\u6362\u4e3a\u2026", None))
        self.deleteDatasetButton.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u2026", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u63d0\u53d6\u90e8\u5206\u5206\u7c7b\u2026", None))
        self.cleanDatasetButton.setText(QCoreApplication.translate("Form", u"\u6e05\u7406\u2026", None))
    # retranslateUi


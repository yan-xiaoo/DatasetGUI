# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowCWCvRc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.action_new_dataset = QAction(MainWindow)
        self.action_new_dataset.setObjectName(u"action_new_dataset")
        self.action_add_dataset = QAction(MainWindow)
        self.action_add_dataset.setObjectName(u"action_add_dataset")
        self.action_delete_dataset = QAction(MainWindow)
        self.action_delete_dataset.setObjectName(u"action_delete_dataset")
        self.action_detail = QAction(MainWindow)
        self.action_detail.setObjectName(u"action_detail")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(17)
        self.groupBox.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.main_table = QTableWidget(self.groupBox)
        if (self.main_table.columnCount() < 3):
            self.main_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.main_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.main_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.main_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.main_table.setObjectName(u"main_table")
        self.main_table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.main_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.main_table.setAlternatingRowColors(True)
        self.main_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.main_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.main_table.setSortingEnabled(True)
        self.main_table.horizontalHeader().setMinimumSectionSize(60)
        self.main_table.horizontalHeader().setDefaultSectionSize(150)
        self.main_table.horizontalHeader().setStretchLastSection(True)
        self.main_table.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.main_table)


        self.verticalLayout.addWidget(self.groupBox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_add_dataset)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u96c6\u7ba1\u7406", None))
        self.action_new_dataset.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u7a7a\u767d\u6570\u636e\u96c6\u2026", None))
#if QT_CONFIG(tooltip)
        self.action_new_dataset.setToolTip(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u7a7a\u767d\u6570\u636e\u96c6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_new_dataset.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.action_add_dataset.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u6570\u636e\u96c6\u2026", None))
#if QT_CONFIG(tooltip)
        self.action_add_dataset.setToolTip(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u4e00\u4e2a\u5df2\u5b58\u5728\u7684\u6570\u636e\u96c6", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_add_dataset.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.action_delete_dataset.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u6570\u636e\u96c6\u2026", None))
        self.action_detail.setText(QCoreApplication.translate("MainWindow", u"\u8be6\u60c5\u2026", None))
#if QT_CONFIG(tooltip)
        self.action_detail.setToolTip(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u67e5\u770b\u8be6\u60c5", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u96c6\u7ba1\u7406", None))
        ___qtablewidgetitem = self.main_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u540d\u79f0", None));
        ___qtablewidgetitem1 = self.main_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u7c7b\u578b", None));
        ___qtablewidgetitem2 = self.main_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u4f4d\u7f6e", None));
#if QT_CONFIG(tooltip)
        self.main_table.setToolTip(QCoreApplication.translate("MainWindow", u"\u53cc\u51fb\u4e00\u884c\u6216\u53f3\u952e\u5e76\u9009\u62e9\u201c\u8be6\u60c5\u201d\u53ef\u4ee5\u8fdb\u5165\u7ba1\u7406\u754c\u9762", None))
#endif // QT_CONFIG(tooltip)
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
    # retranslateUi


import os.path

from PySide2.QtWidgets import QMainWindow, QTableWidgetItem, QMenu
from PySide2.QtCore import QPoint, Slot
from ..Ui.ui_main_window import Ui_MainWindow
from .. import dataset_config
from .add_dataset_dialog import AddDatasetDialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        if os.path.exists("dataset/config.json"):
            self.dataset_manager = dataset_config.DatasetManager.load("dataset/config.json")
        else:
            self.dataset_manager = dataset_config.DatasetManager()
        for one_dataset in self.dataset_manager:
            self.add_dataset_to_display(config=one_dataset)

        self.context_menu = QMenu(self)
        self.context_menu.addActions([self.action_detail, self.action_delete_dataset])
        self.main_table.customContextMenuRequested.connect(self.contextMenu)

    def add_dataset(self, config: dataset_config.DatasetConfig, row=None):
        self.dataset_manager.append(config)
        self.add_dataset_to_display(config, row)

    def add_dataset_to_display(self, config: dataset_config.DatasetConfig, row=None):
        if row is None:
            row = self.main_table.rowCount()
        self.main_table.insertRow(row)
        name = QTableWidgetItem(config.name)
        type_ = QTableWidgetItem(config.type_.upper())
        label_path = QTableWidgetItem(config.label_path)
        self.main_table.setItem(row, 0, name)
        self.main_table.setItem(row, 1, type_)
        self.main_table.setItem(row, 2, label_path)

    def contextMenu(self, pos: QPoint):
        self.context_menu.exec_(self.main_table.mapToGlobal(pos))

    @Slot()
    def on_action_add_dataset_triggered(self):
        add_dataset = AddDatasetDialog(self)
        add_dataset.exec_()

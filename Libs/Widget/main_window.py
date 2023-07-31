import os.path

from PySide2.QtWidgets import QMainWindow, QTableWidgetItem, QMenu
from PySide2.QtCore import QPoint, Slot
from ..Ui.ui_main_window import Ui_MainWindow
from .. import dataset_config
from .. import changelog
from .common_dialog import CommonDialog
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

        self.check_datasets()

    def add_dataset(self, config: dataset_config.DatasetConfig, row=None):
        self.dataset_manager.append(config)
        self.add_dataset_to_display(config, row)
        self.check_datasets()

    @staticmethod
    def check_dataset_exist(config: dataset_config.DatasetConfig):
        if config.type_ == 'coco':
            if not os.path.isdir(config.image_path) and not os.path.isfile(config.label_path):
                return False
        elif config.type_ == 'yolo':
            if not os.path.isdir(config.image_path) and not os.path.isdir(config.label_path):
                return False
        return True

    def check_datasets(self):
        lost = []
        for dataset in self.dataset_manager[:]:
            if not self.check_dataset_exist(dataset):
                index = self.dataset_manager.index(dataset)
                self.delete_dataset_from_display(index)
                self.dataset_manager.remove(dataset)
                id_ = dataset_config.get_id_by_config(dataset)
                if id_ is not None:
                    changelog.delete_changelog(id_)
                lost.append(f"名为 {dataset.name} 的数据集")
        if lost:
            dialog = CommonDialog(self, "数据集丢失", "以下数据集的图片与标签均已丢失。它们已被从记录中移除。",
                                  "\n".join(lost), ["确定", "确定"])
            dialog.exec_()

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

    def delete_dataset_from_display(self, row):
        self.main_table.removeRow(row)

    def contextMenu(self, pos: QPoint):
        self.context_menu.exec_(self.main_table.mapToGlobal(pos))

    @Slot()
    def on_action_add_dataset_triggered(self):
        add_dataset = AddDatasetDialog(self)
        if add_dataset.exec_() == add_dataset.Accepted:
            self.add_dataset(add_dataset.config)

import shutil

from ..Ui.ui_divide_dataset_dialog import Ui_Dialog
from PySide2.QtWidgets import QDialog, QMessageBox
from PySide2.QtCore import Slot
from .common_dialog import CommonDialog
from ..work_functions import CopyCertainImage
from ..process_window import ProcessWindow
from ..Dataset.split_coco import category_split
from ..Dataset.split_yolo import basic_split
from ..Dataset.yolo_to_coco import YoloSearch
from .. import dataset_config
from ..changelog import ChangeLog
import json
import os


class DivideDatasetDialog(QDialog, Ui_Dialog):
    def __init__(self, config, parent=None):
        super().__init__(parent)
        self.config = config
        self.setupUi(self)
        self.trainEdit.setText(self.config.name + "_训练")
        self.valEdit.setText(self.config.name + "_验证")
        self.train_config = self.val_config = None
        self.trainBox.valueChanged.connect(self.trainBox_valueChanged)
        self.valBox.valueChanged.connect(self.valBox_valueChanged)

    @Slot()
    def trainBox_valueChanged(self, value):
        self.valBox.setValue(100 - value)

    @Slot()
    def valBox_valueChanged(self, value):
        self.trainBox.setValue(100 - value)

    @Slot()
    def on_okButton_clicked(self):
        if not self.trainEdit.text():
            QMessageBox.warning(self, "警告", "请您为新的训练集起名")
            return
        if not self.valEdit.text():
            QMessageBox.warning(self, "警告", "请您为新的验证集起名")
            return

        dialog = CommonDialog(self, "删除时的问题", "删除时两数据集会被一同删除",
                              "训练集与验证集在删除时只能同时被删除\n"
                              "删除一个数据集的文件时会同时删除另一个的文件")
        if dialog.exec_() == dialog.Rejected:
            return

        if self.config.type_ == 'coco':
            train_file, val_file = category_split(self.config.label_path, int(self.trainBox.value()) / 100,
                                                  int(self.valBox.value()) / 100)
            id_ = dataset_config.get_available_id()
            train_images = [one['file_name'] for one in train_file.dataset['images']]
            thread = CopyCertainImage(self.config.image_path, train_images, f"dataset/{id_}/images/train",
                                      id_, "正在复制训练集图片")
            window = ProcessWindow(thread, self, "拷贝训练集图片", stoppable=True)
            if window.exec_() == window.Rejected:
                return
            val_images = [one['file_name'] for one in val_file.dataset['images']]
            thread = CopyCertainImage(self.config.image_path, val_images, f"dataset/{id_}/images/val",
                                      id_, "正在复制验证集图片")
            window = ProcessWindow(thread, self, "拷贝验证集图片", stoppable=True)
            if window.exec_() == window.Rejected:
                return
            change_log = ChangeLog.load(id_)
            with open(f"dataset/{id_}/train.json", "w") as f:
                json.dump(train_file.dataset, f, indent=4, ensure_ascii=False)
                change_log.append(f"dataset/{id_}/train.json")
            with open(f"dataset/{id_}/val.json", "w") as f:
                json.dump(val_file.dataset, f, indent=4, ensure_ascii=False)
                change_log.append(f"dataset/{id_}/val.json")
            change_log.save(id_)

            self.train_config = dataset_config.CocoDataset(self.trainEdit.text(),f"dataset/{id_}/images/train", f"dataset/{id_}/train.json")
            self.val_config = dataset_config.CocoDataset(self.valEdit.text(), f"dataset/{id_}/images/val", f"dataset/{id_}/val.json")
            dataset_config.MergedDatasetConfig(self.train_config, self.val_config)
        else:
            train_labels, val_labels = basic_split(self.config.label_path, int(self.trainBox.value()) / 100,
                                                   int(self.valBox.value()) / 100)
            search = YoloSearch(self.config.image_path)
            train_images = []
            for one in train_labels:
                result = search.search(one)
                train_images.append(result)
                print(f"Generating {result} from {one}")
            val_images = [search.search(one) for one in val_labels]
            id_ = dataset_config.get_available_id()
            thread = CopyCertainImage(self.config.label_path, train_labels, f"dataset/{id_}/labels/train", id_, "正在复制训练集标签")
            window = ProcessWindow(thread, self, "正在拷贝训练集标签", stoppable=True)
            if window.exec_() == window.Rejected:
                return
            thread = CopyCertainImage(self.config.label_path, val_labels, f"dataset/{id_}/labels/val", id_,
                                      "正在复制验证集标签")
            window = ProcessWindow(thread, self, "正在拷贝验证集标签", stoppable=True)
            if window.exec_() == window.Rejected:
                return
            thread = CopyCertainImage(self.config.image_path, train_images, f"dataset/{id_}/images/train", id_,
                                      "正在复制训练集图片")
            window = ProcessWindow(thread, self, "正在拷贝训练集图片", stoppable=True)
            if window.exec_() == window.Rejected:
                return
            thread = CopyCertainImage(self.config.image_path, val_images, f"dataset/{id_}/images/val", id_,
                                      "正在复制验证集图片")
            window = ProcessWindow(thread, self, "正在拷贝验证集图片", stoppable=True)
            if window.exec_() == window.Rejected:
                return
            change_log = ChangeLog.load(id_)
            try:
                shutil.copyfile(os.path.join(self.config.label_path, "classes.txt"), f"dataset/{id_}/labels/train/classes.txt")
            except FileNotFoundError:
                pass
            else:
                change_log.append(f"dataset/{id_}/labels/train/classes.txt")
            try:
                shutil.copyfile(os.path.join(self.config.label_path, "classes.txt"),
                                f"dataset/{id_}/labels/val/classes.txt")
            except FileNotFoundError:
                pass
            else:
                change_log.append(f"dataset/{id_}/labels/val/classes.txt")
            change_log.save(id_)

            self.train_config = dataset_config.YoloDataset(self.trainEdit.text(), f"dataset/{id_}/images/train",
                                                           f"dataset/{id_}/labels/train")
            self.val_config = dataset_config.YoloDataset(self.valEdit.text(), f"dataset/{id_}/images/val",
                                                         f"dataset/{id_}/labels/val")
            dataset_config.MergedDatasetConfig(self.train_config, self.val_config)

        self.accept()


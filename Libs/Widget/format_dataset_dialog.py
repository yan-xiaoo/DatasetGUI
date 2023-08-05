import os.path

from ..Ui.ui_format_dataset_dialog import Ui_Dialog
from PySide2.QtWidgets import QDialog, QMessageBox
from .. import dataset_config
from ..Dataset.yolo_to_coco import yolo_to_coco
from .common_dialog import CommonDialog
from PySide2.QtCore import Slot


class FormatDatasetDialog(QDialog, Ui_Dialog):
    def __init__(self, config: dataset_config.DatasetConfig, parent=None):
        super().__init__(parent)
        self.config = config
        self.new_config = None
        self.setupUi(self)

        if self.config.data_type == dataset_config.DataType.TRAIN:
            self.mergeBox.setText("同时转换验证集")
            self.mergeBox.setChecked(True)
        elif self.config.data_type == dataset_config.DataType.VAL:
            self.mergeBox.setText("同时转换训练集")
            self.mergeBox.setChecked(True)
        else:
            self.mergeBox.setChecked(False)
            self.mergeBox.setVisible(False)
        if self.config.type_ == 'coco':
            self.typeButton.setText("YOLO格式的数据集")
        else:
            self.typeButton.setText("COCO格式的数据集")
        self.nameEdit.setText(self.config.name.removesuffix("_训练").removesuffix("_验证"))
        self.adjustSize()

    @Slot()
    def on_okButton_clicked(self):
        if not self.nameEdit.text():
            QMessageBox.warning(self, "警告", "请为您的新数据集起个名字")
            return
        if self.config.type_ == 'coco':
            if self.mergeBox.checkState():
                pass
            else:
                pass
        elif self.config.type_ == 'yolo':
            if self.mergeBox.checkState():
                if not os.path.isfile(os.path.join(self.config.parent.train.label_path, "classes.txt")):
                    dialog = CommonDialog(self, "训练集中没有分类", "训练集中不存在分类信息",
                                          "您的YOLO训练集中不存在classes.txt。请创建一个\n"
                                          "classes.txt文件应放在您的标签文件夹下，每行都是一个类别的名称",
                                          ["返回", "返回"])
                    dialog.exec_()
                    return
                if not os.path.isfile(os.path.join(self.config.parent.val.label_path, "classes.txt")):
                    dialog = CommonDialog(self, "验证集中没有分类", "验证集中不存在分类信息",
                                          "您的YOLO验证集中不存在classes.txt。请创建一个\n"
                                          "classes.txt文件应放在您的标签文件夹下，每行都是一个类别的名称",
                                          ["返回", "返回"])
                    dialog.exec_()
                    return
                id_ = dataset_config.get_available_id()
                if yolo_to_coco(self.config.parent.train.image_path, self.config.parent.train.label_path,
                                f"dataset/{id_}/images/train", f"dataset/{id_}/train.json",
                                id_) == 1:
                    return
                if yolo_to_coco(self.config.parent.val.image_path, self.config.parent.val.label_path,
                                f"dataset/{id_}/images/val", f"dataset/{id_}/val.json", id_) == 1:
                    return
                self.new_config = dataset_config.MergedDatasetConfig(
                    dataset_config.CocoDataset(self.nameEdit.text() + "_训练", f"dataset/{id_}/images/train",f'dataset/{id_}/train.json'),
                    dataset_config.CocoDataset(self.nameEdit.text() + "_验证", f"dataset/{id_}/images/val", f"dataset/{id_}/val.json")
                )
            else:
                if not os.path.isfile(os.path.join(self.config.label_path, "classes.txt")):
                    dialog = CommonDialog(self, "数据集中没有分类", "数据集中不存在分类信息",
                                          "您的YOLO数据集中不存在classes.txt。请创建一个\n"
                                          "classes.txt文件应放在您的标签文件夹下，每行都是一个类别的名称",
                                          ["返回", "返回"])
                    dialog.exec_()
                    return
                id_ = dataset_config.get_available_id()
                if yolo_to_coco(self.config.image_path, self.config.label_path,
                                f"dataset/{id_}/images", f"dataset/{id_}/dataset.json",
                                id_) == 1:
                    return
                self.new_config = dataset_config.CocoDataset(self.nameEdit.text(),
                                                             f"dataset/{id_}/images", f"dataset/{id_}/dataset.json")

        self.accept()

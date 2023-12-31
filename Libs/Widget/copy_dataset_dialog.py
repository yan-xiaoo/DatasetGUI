import os.path
import shutil

from ..Ui.ui_copy_dataset_dialog import Ui_Dialog
from ..dataset_config import DatasetConfig, get_available_id, DataType, MergedDatasetConfig, YoloDataset, CocoDataset
from ..process_window import ProcessWindow
from ..work_functions import CopyDir
from ..changelog import ChangeLog
from .common_dialog import CommonDialog
from PySide2.QtWidgets import QDialog, QFileDialog, QMessageBox
from PySide2.QtCore import Slot


class CopyDatasetDialog(QDialog, Ui_Dialog):
    def __init__(self, config: DatasetConfig, parent=None):
        super().__init__(parent)
        self.config = config
        self.new_config = None
        self.setupUi(self)
        self.on_setRadioButton_clicked()

        if config.data_type == DataType.TRAIN:
            self.copyMergeBox.setText("同时拷贝验证集")
        elif config.data_type == DataType.VAL:
            self.copyMergeBox.setText("同时拷贝训练集")
        else:
            self.copyMergeBox.setVisible(False)
            self.copyMergeBox.setChecked(False)
            self.adjustSize()

    @Slot()
    def on_setRadioButton_clicked(self):
        self.imagePathEdit.setEnabled(False)
        self.labelPathEdit.setEnabled(False)
        self.imageButton.setEnabled(False)
        self.labelButton.setEnabled(False)

    @Slot()
    def on_freeRadioButton_clicked(self):
        self.imagePathEdit.setEnabled(True)
        self.labelPathEdit.setEnabled(True)
        self.imageButton.setEnabled(True)
        self.labelButton.setEnabled(True)

    @Slot()
    def on_imageButton_clicked(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(dialog.Directory)
        if dialog.exec_():
            self.imagePathEdit.setText(dialog.selectedFiles()[0])

    @Slot()
    def on_labelButton_clicked(self):
        if self.config.type_ == 'coco':
            file_name = QFileDialog.getSaveFileName(self, caption="选择保存文件位置",
                                                    filter="Json Files(*.json);;All files(*.*)")
            if file_name[0]:
                self.labelPathEdit.setText(file_name[0])
        else:
            dialog = QFileDialog(self)
            dialog.setFileMode(dialog.Directory)
            if dialog.exec_():
                self.labelPathEdit.setText(dialog.selectedFiles()[0])

    @Slot()
    def on_okButton_clicked(self):
        if not self.nameEdit.text():
            QMessageBox.warning(self, "警告", "请您为新数据集起一个名字")
            return
        if self.freeRadioButton.isChecked():
            if not self.imagePathEdit.text():
                QMessageBox.warning(self, "警告", "图片文件夹为空")
                return
            if not self.labelPathEdit.text():
                QMessageBox.warning(self, "警告", "标签文件夹为空")
                return
            if not os.path.isdir(self.imagePathEdit.text()):
                QMessageBox.warning(self, "警告", "选择的图片文件夹不存在")
                return
            if self.config.type_ == 'yolo' and not os.path.isdir(self.labelPathEdit.text()):
                QMessageBox.warning(self, "警告", "选择的标签文件夹不存在")
                return
            if self.config.type_ == 'coco' and not os.path.isdir(os.path.dirname(self.labelPathEdit.text())):
                QMessageBox.warning(self, "警告", "选择的标签文件的上层文件夹不存在")
                return

            if self.config.data_type in (DataType.TRAIN, DataType.VAL) and self.copyMergeBox.isChecked():
                dialog = CommonDialog(self, "复制问题", "自选目录时无法同时拷贝训练/验证集",
                                      "不使用默认目录时，无法同时拷贝训练集和验证集。是否仍要继续？",
                                      ['继续', '返回'])
                if dialog.exec_() == dialog.Rejected:
                    return

            image_path = self.imagePathEdit.text()
            label_path = self.labelPathEdit.text()
            d = None
        else:
            d = get_available_id()
            image_path = f"dataset/{d}/images"
            if self.config.type_ == 'yolo':
                label_path = f"dataset/{d}/labels"
            else:
                label_path = f"dataset/{d}/dataset.json"

        if not self.copyMergeBox.checkState():
            name = self.nameEdit.text()
            self.new_config = DatasetConfig.from_type(self.config.type_, {"name": name, "image_path": image_path,
                                                                          "label_path": label_path})

            thread = CopyDir(self.config.image_path, self.new_config.image_path, d, "正在拷贝数据集图片")
            window = ProcessWindow(thread, self, title="正在拷贝数据集图片", stoppable=True)
            if window.exec_() == window.Rejected:
                return
            if self.config.type_ == 'coco' and d is not None:
                log = ChangeLog.load(d)
                log.append(os.path.abspath(self.new_config.label_path))
                shutil.copyfile(self.config.label_path, self.new_config.label_path)
                log.save(d)
            else:
                thread = CopyDir(self.config.label_path, self.new_config.label_path, d, "正在拷贝数据集标签")
                window = ProcessWindow(thread, self, title="正在拷贝数据集标签", stoppable=True)
                if window.exec_() == window.Rejected:
                    return

        elif self.copyMergeBox.checkState() and self.config.data_type in [DataType.TRAIN, DataType.VAL]:
            id_ = get_available_id()
            train_image_path = f"dataset/{id_}/images/train"
            val_image_path = f"dataset/{id_}/images/val"
            if self.config.type_ == 'yolo':
                train_label_path = f"dataset/{id_}/labels/train"
                val_label_path = f"dataset/{id_}/labels/val"
                self.new_config = MergedDatasetConfig(
                    YoloDataset(self.nameEdit.text() + "_训练", train_image_path, train_label_path),
                    YoloDataset(self.nameEdit.text() + "_验证", val_image_path, val_label_path))
            else:
                train_label_path = f"dataset/{id_}/train.json"
                val_label_path = f"dataset/{id_}/val.json"
                self.new_config = MergedDatasetConfig(
                    CocoDataset(self.nameEdit.text() + "_训练", train_image_path, train_label_path),
                    CocoDataset(self.nameEdit.text() + "_验证", val_image_path, val_label_path))

            if self.config.type_ == 'coco':
                thread = CopyDir(self.config.parent.train.image_path, train_image_path, id_, "正在拷贝训练集图片")
                window = ProcessWindow(thread, self, title="正在拷贝训练集图片", stoppable=True)
                if window.exec_() == window.Rejected:
                    return
                thread = CopyDir(self.config.parent.val.image_path, val_image_path, id_, "正在拷贝验证集图片")
                window = ProcessWindow(thread, self, title="正在拷贝验证集图片", stoppable=True)
                if window.exec_() == window.Rejected:
                    return
                log = ChangeLog.load(id_)
                log.append(os.path.abspath(train_label_path))
                log.append(os.path.abspath(val_label_path))
                shutil.copyfile(self.config.parent.train.label_path, train_label_path)
                shutil.copyfile(self.config.parent.val.label_path, val_label_path)
                log.save(id_)
            elif self.config.type_ == 'yolo':
                thread = CopyDir(self.config.parent.train.image_path, train_image_path, id_, "正在拷贝训练集图片")
                window = ProcessWindow(thread, self, title="正在拷贝训练集图片", stoppable=True)
                if window.exec_() == window.Rejected:
                    return
                thread = CopyDir(self.config.parent.val.image_path, val_image_path, id_, "正在拷贝验证集图片")
                window = ProcessWindow(thread, self, title="正在拷贝验证集图片", stoppable=True)
                if window.exec_() == window.Rejected:
                    return
                thread = CopyDir(self.config.parent.train.label_path, train_label_path, id_, "正在拷贝训练集标签")
                window = ProcessWindow(thread, self, title="正在拷贝训练集标签", stoppable=True)
                if window.exec_() == window.Rejected:
                    return
                thread = CopyDir(self.config.parent.val.label_path, val_label_path, id_, "正在拷贝验证集标签")
                window = ProcessWindow(thread, self, title="正在拷贝验证集标签", stoppable=True)
                if window.exec_() == window.Rejected:
                    return

        self.accept()

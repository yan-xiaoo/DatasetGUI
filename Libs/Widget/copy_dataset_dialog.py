import os.path
import shutil

from ..Ui.ui_copy_dataset_dialog import Ui_Dialog
from ..dataset_config import DatasetConfig, get_available_id
from ..process_window import ProcessWindow
from ..work_functions import CopyDir
from ..changelog import ChangeLog
from PySide2.QtWidgets import QDialog, QFileDialog, QMessageBox
from PySide2.QtCore import Slot


class CopyDatasetDialog(QDialog, Ui_Dialog):
    def __init__(self, config, parent=None):
        super().__init__(parent)
        self.config = config
        self.new_config = None
        self.setupUi(self)
        self.on_setRadioButton_clicked()

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
            QMessageBox.warning(self, "警告", "请您为数据集起一个名字")
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
        name = self.nameEdit.text()
        self.new_config = DatasetConfig.from_type(self.config.type_, {"name": name, "image_path": image_path,
                                                                      "label_path": label_path})

        thread = CopyDir(self.config.image_path, self.new_config.image_path, d, "正在拷贝数据集图片")
        window = ProcessWindow(thread, self, title="正在拷贝数据集图片", stoppable=True)
        if window.exec_() == window.Rejected:
            return
        if self.config.type_ == 'coco':
            log = ChangeLog.load(d)
            log.append(os.path.abspath(self.new_config.label_path))
            shutil.copyfile(self.config.label_path, self.new_config.label_path)
        else:
            thread = CopyDir(self.config.label_path, self.new_config.label_path, d, "正在拷贝数据集标签")
            window = ProcessWindow(thread, self, title="正在拷贝数据集标签", stoppable=True)
            if window.exec_() == window.Rejected:
                return

        self.accept()

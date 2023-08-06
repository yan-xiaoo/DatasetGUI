import os
from ..Ui.ui_clean_dataset_dialog import Ui_Dialog
from PySide2.QtWidgets import QDialog, QMessageBox
from PySide2.QtCore import Slot
from .check_result_dialog import CheckResultDialog
from ..Dataset import clean_coco, clean_yolo
from .. import dataset_config
from filetype import is_image
from ..process_window import ProcessWindow, ProcessFunction


class CheckDatasetDialog(QDialog, Ui_Dialog):
    def __init__(self, config: dataset_config.DatasetConfig, parent=None):
        super().__init__(parent)
        self.config = config
        self.setupUi(self)

    @Slot()
    def on_okButton_clicked(self):
        result1 = result2 = result3 = 0
        if self.labelCheckBox.isChecked():
            result1 = self.check_label()
            if result1 == 0:
                QMessageBox.information(self, "检查结果", "数据集中没有冗余的数据")
        if self.imageCheckBox.isChecked():
            result2 = self.check_image()
            if result2 == 0:
                QMessageBox.information(self, "检查结果", "数据集中的标签对应的图片文件均存在")
        if self.fileCheckBox.isChecked():
            result3 = self.check_file()
            if result3 == 0:
                QMessageBox.information(self, "检查结果", "数据集文件夹下没有多余文件")

    def check_label(self):
        if self.config.type_ == 'coco':
            result = clean_coco.check_coco_detailed(self.config.label_path)
            if result:
                dialog = CheckResultDialog(result, parent=self, clean_slot=lambda: clean_coco.clean(self.config.label_path))
                dialog.exec_()
                return 1
            else:
                return 0
        else:
            thread = clean_yolo.CheckYoloDataset(self.config.image_path, self.config.label_path)
            window = ProcessWindow(thread, self, "检查YOLO数据集")
            if window.exec_() == window.Rejected:
                return 1
            if thread.result:
                dialog = CheckResultDialog(thread.result, parent=self)
                dialog.exec_()
                return 1
            else:
                return 0

    def check_image(self):
        if self.config.type_ == 'coco':
            result = clean_coco.check_coco_images(self.config.image_path, self.config.label_path)
            if result:
                dialog = CheckResultDialog(result, parent=self)
                dialog.exec_()
                return 1
            else:
                return 0
        else:
            result = clean_yolo.check_yolo_images(self.config.image_path, self.config.label_path)
            if result:
                dialog = CheckResultDialog(result, parent=self)
                dialog.exec_()
                return 1
            else:
                return 0

    def check_file(self):
        if self.config.type_ == 'coco':
            result = CheckExtraFile(self.config.image_path, is_image)
            window = ProcessWindow(result, self, "检查数据集中多余的文件")
            if window.exec_() == window.Rejected:
                return 1
            if result.result:
                dialog = CheckResultDialog(result.result, parent=self)
                dialog.exec_()
                return 1
            else:
                return 0
        else:
            thread = CheckExtraFile(self.config.image_path, is_image)
            window = ProcessWindow(thread, self, "检查数据集中多余的文件")
            if window.exec_() == window.Rejected:
                return 1
            result = thread.result.copy()
            thread = CheckExtraFile(self.config.label_path, is_yolo_file)
            window = ProcessWindow(thread, self, "检查数据集中多余的文件")
            if window.exec_() == window.Rejected:
                return 1
            result.extend(thread.result)
            if result:
                dialog = CheckResultDialog(result, parent=self)
                dialog.exec_()
                return 1
            return 0


class CheckExtraFile(ProcessFunction):
    def __init__(self, dst, checker_func, hint="正在检查数据集中多余的文件"):
        super().__init__()
        self.dst = dst
        self.checker_func = checker_func
        self.result = []
        self.hint = hint

    def run(self) -> None:
        self.setText.emit(self.hint)
        length = len(os.listdir(self.dst))
        self.setMaximum.emit(length)
        for index, file in enumerate(os.listdir(self.dst)):
            self.setProgress.emit(index + 1)
            self.setDetailedText.emit(f"正在检查 {file} {index + 1}/{length}")
            try:
                result = self.checker_func(os.path.join(self.dst, file))
            except Exception:
                result = False
            if not result:
                self.result.append(f"{self.dst} 下存在错误文件 {file}")
        self.has_finished.emit()


def is_yolo_file(path):
    result = True
    if os.path.basename(path) == "classes.txt":
        return True
    try:
        with open(path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line == "":
                    continue
                line = line.split(' ')
                if (len(line) - 5) % 2 != 0 or len(line) < 5:
                    result = False
                    break
    except Exception:
        result = False
    return result

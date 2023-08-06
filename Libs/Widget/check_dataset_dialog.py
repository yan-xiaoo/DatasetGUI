from ..Ui.ui_clean_dataset_dialog import Ui_Dialog
from PySide2.QtWidgets import QDialog, QMessageBox
from PySide2.QtCore import Slot
from .check_result_dialog import CheckResultDialog
from ..Dataset import clean_coco, clean_yolo
from .. import dataset_config
from ..process_window import ProcessWindow


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
        if self.imageCheckBox.isChecked():
            result2 = self.check_image()
        if self.fileCheckBox.isChecked():
            result3 = self.check_file()
        if result1 == result2 == result3 == 0:
            QMessageBox.information(self, "检查完成", "数据集检查完成，没有发现问题")
            self.accept()

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
            pass
        else:
            pass

    def check_file(self):
        if self.config.type_ == 'coco':
            pass
        else:
            pass

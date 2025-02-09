from PySide2.QtWidgets import QDialog, QMessageBox
from PySide2.QtGui import QIntValidator
from ..dataset_config import DatasetConfig
from PySide2.QtCore import Slot
from ..process_window import ProcessWindow
from ..Dataset.check_keypoints import *
from .common_dialog import CommonDialog
from ..Ui.ui_keypoint_number_dialog import Ui_dialog


class KeypointNumberDialog(QDialog, Ui_dialog):
    def __init__(self, dataset: DatasetConfig, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.dataset = dataset
        self.result = []
        self.class_keypoint = {}
        if dataset.type_ == "yolo":
            try:
                classes = get_yolo_classes(os.path.join(self.dataset.label_path, "classes.txt"))
            except FileNotFoundError:
                QMessageBox.critical(self, "错误", "未找到类别文件，请检查数据集标签路径下是否包含 classes.txt 文件")
                self.reject()
                return

            for one_class_name in classes.values():
                self.classesList.addItem(one_class_name)

        elif dataset.type_ == 'coco':
            coco = COCO(dataset.label_path)
            for one_name in coco.cats.values():
                self.classesList.addItem(one_name['name'])

        self.numberEdit.setValidator(QIntValidator(1, 999999, self.numberEdit))

        self.classesList.setCurrentRow(0)
        self.adjustSize()

    @Slot()
    def on_numberEdit_textEdited(self):
        current = self.classesList.currentRow()
        if current != -1:
            try:
                self.class_keypoint[current] = int(self.numberEdit.text())
            except ValueError:
                pass

    @Slot()
    def on_classesList_itemSelectionChanged(self):
        current = self.classesList.currentRow()
        if current != -1:
            try:
                self.numberEdit.setText(str(self.class_keypoint[current]))
            except KeyError:
                self.numberEdit.clear()

    @Slot()
    def on_okButton_clicked(self):
        if len(self.class_keypoint.keys()) == 0:
            QMessageBox.critical(self, "错误", "请至少输入一个类别的关键点数量")
            return

        for index in range(self.classesList.count()):
            if index not in self.class_keypoint.keys():
                dialog = CommonDialog(self, "输入确认", "有些类别的关键点数量尚未输入",
                                      "如果继续，那么将不会检查这些类别的关键点\n个数是否正确。是否仍然继续？")
                if dialog.exec_() == dialog.Rejected:
                    return
                else:
                    break

        if self.dataset.type_ == 'coco':
            coco = COCO(self.dataset.label_path)
            coco_categories = [i['id'] for i in coco.dataset['categories']]
            if 0 in coco_categories or '0' in coco_categories:
                class_keypoint = {i: j for i, j in self.class_keypoint.items()}
            else:
                class_keypoint = {i + 1: j for i, j in self.class_keypoint.items()}
            self.result = get_coco_keypoints(self.dataset.label_path, class_keypoint)
        elif self.dataset.type_ == 'yolo':
            class_keypoint = {i: j for i, j in self.class_keypoint.items()}
            work = CheckYoloKeyPoints(self.dataset, class_keypoint)
            window = ProcessWindow(work, self, title="正在检查关键点数量", stoppable=True)
            if window.exec_() == window.Rejected:
                return
            self.result = work.wrong_images

        self.accept()

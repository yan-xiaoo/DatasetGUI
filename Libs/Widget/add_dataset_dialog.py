import os

from ..Ui.ui_add_dataset_dialog import Ui_Dialog
from .common_dialog import CommonDialog
from ..work_functions import CopyDir
from ..process_window import ProcessWindow
from .. import dataset_config
from PySide2.QtWidgets import QDialog, QFileDialog, QMessageBox
from PySide2.QtCore import Slot


class AddDatasetDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.on_currentIndexChanged(0)
        self.datasetTypeBox.currentIndexChanged.connect(self.on_currentIndexChanged)

    @Slot()
    def on_currentIndexChanged(self, index):
        if index == 0:
            self.yoloBox.setVisible(False)
            self.cocoBox.setVisible(True)
        else:
            self.yoloBox.setVisible(True)
            self.cocoBox.setVisible(False)

    @Slot()
    def on_cocoImageButton_clicked(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec_():
            self.cocoImageEdit.setText(dialog.selectedFiles()[0])

    @Slot()
    def on_cocoLabelButton_clicked(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilters(["Json Files(*.json)", "All files(*.*)"])
        if dialog.exec_():
            self.cocoLabelEdit.setText(dialog.selectedFiles()[0])

    @Slot()
    def on_yoloImageButton_clicked(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec_():
            self.yoloImageEdit.setText(dialog.selectedFiles()[0])

    @Slot()
    def on_yoloLabelButton_clicked(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec_():
            self.yoloLabelEdit.setText(dialog.selectedFiles()[0])

    @Slot()
    def on_okButton_clicked(self):
        if self.datasetTypeBox.currentIndex() == 0:
            type_ = 'coco'
        else:
            type_ = 'yolo'

        if type_ == 'coco':
            if not self.cocoName.text():
                QMessageBox.warning(self, "警告", "请您为数据集取一个名字")
                return
            if not self.cocoImageEdit.text():
                QMessageBox.warning(self, "警告", "请选择数据集图片文件夹")
                return
            if not os.path.isdir(self.cocoImageEdit.text()):
                QMessageBox.warning(self, "警告", "您选择的图片文件夹不存在")
                return
            if not self.cocoLabelEdit.text():
                QMessageBox.warning(self, "警告", "请选择数据集标签文件")
                return
            if not os.path.isfile(self.cocoLabelEdit.text()):
                QMessageBox.warning(self, "警告", "您选择的标签文件不存在")
                return
        elif type_ == 'yolo':
            if not self.yoloName.text():
                QMessageBox.warning(self, "警告", "请您为数据集取一个名字")
                return
            if not self.yoloImageEdit.text():
                QMessageBox.warning(self, "警告", "请选择数据集图片文件夹")
                return
            if not os.path.isdir(self.yoloImageEdit.text()):
                QMessageBox.warning(self, "警告", "您选择的图片文件夹不存在")
                return
            if not self.yoloLabelEdit.text():
                QMessageBox.warning(self, "警告", "请选择数据集标签文件夹")
                return
            if not os.path.isdir(self.yoloLabelEdit.text()):
                QMessageBox.warning(self, "警告", "您选择的标签文件夹不存在")
                return

        if self.copyDatasetBox.checkState():
            pass
        else:
            warn = CommonDialog(self, "警告", "删除该数据集时存在安全隐患",
                                "如果您不复制该数据集，则删除该数据集时，无法自动删除数据集文件\n"
                                "这是因为，我们无法确定数据集中哪部分是真正的数据，哪部分是您的文件\n"
                                "直接删除的话，您的数据很可能被误删\n"
                                "您可以点击“返回”并勾选“拷贝数据集”来解决这个问题\n", ("仍然继续", "返回"))
            warn.cancelButton.setFocus()
            if warn.exec_() == warn.Accepted:
                print("仍然继续")
            else:
                return

        d = dataset_config.get_available_id()
        thread = CopyDir(self.cocoImageEdit.text(), f"dataset/{d}/images", d, "正在复制数据集图片")
        window = ProcessWindow(thread, self, title="复制数据集", stoppable=True)
        window.exec_()

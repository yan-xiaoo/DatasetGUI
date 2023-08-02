import os.path

from ..Ui.ui_dataset_window import Ui_Form
from .common_dialog import CommonDialog
from .delete_dataset_dialog import DeleteDatasetDialog
from ..Dataset.clean_coco import clean
from .copy_dataset_dialog import CopyDatasetDialog
from .archive_dataset_dialog import ArchiveDatasetDialog
from .divide_dataset_dialog import DivideDatasetDialog
from PySide2.QtWidgets import QWidget, QFileDialog, QMessageBox
from PySide2.QtCore import Qt, Slot, QUrl
from PySide2.QtGui import QDesktopServices


class DatasetWindow(QWidget, Ui_Form):
    def __init__(self, config, master):
        super().__init__()
        self.setupUi(self)
        self.setAttribute(Qt.WA_QuitOnClose, False)

        self.config = config
        self.master = master
        self.sync_with_config(config)

    def sync_with_config(self, config=None):
        if config is None:
            config = self.config
        self.nameEdit.setText(config.name)
        self.imagePathEdit.setText(config.image_path)
        self.labelPathEdit.setText(config.label_path)
        self.dataTypeLabel.setText(f"{config.type_} 格式的数据集")
        if config.type_ != 'coco':
            self.cleanDatasetButton.setVisible(False)
        else:
            self.cleanDatasetButton.setVisible(True)

    @Slot()
    def on_browseImagePath_clicked(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(dialog.Directory)
        if dialog.exec_():
            self.imagePathEdit.setText(dialog.selectedFiles()[0])

    @Slot()
    def on_browseLabelPath_clicked(self):
        if self.config.type_ == 'coco':
            dialog = QFileDialog(self)
            dialog.setFileMode(dialog.ExistingFile)
            dialog.setNameFilters(["Json Files(*.json)", "All files(*.*)"])
            if dialog.exec_():
                self.labelPathEdit.setText(dialog.selectedFiles()[0])
        else:
            dialog = QFileDialog(self)
            dialog.setFileMode(dialog.Directory)
            if dialog.exec_():
                self.labelPathEdit.setText(dialog.selectedFiles()[0])

    @Slot()
    def on_showImagePathButton_clicked(self):
        service = QDesktopServices()
        service.openUrl(QUrl.fromLocalFile(self.imagePathEdit.text()))

    @Slot()
    def on_showLabelPathButton_clicked(self):
        service = QDesktopServices()
        service.openUrl(QUrl.fromLocalFile(self.labelPathEdit.text()))

    @Slot()
    def on_update_info_clicked(self):
        if not self.nameEdit.text():
            QMessageBox.warning(self, "警告", "请您为数据集起一个名字")
            return
        if not self.imagePathEdit.text():
            QMessageBox.warning(self, "警告", "请您选择图片路径")
            return
        if not self.labelPathEdit.text():
            QMessageBox.warning(self, "警告", "请您选择标签路径")
            return
        if not os.path.isdir(self.imagePathEdit.text()):
            QMessageBox.warning(self, "警告", "您选择的图片文件夹不存在")
            return
        if self.config.type_ == 'coco':
            if not os.path.isfile(self.labelPathEdit.text()):
                QMessageBox.warning(self, "警告", "您选择的标签文件不存在")
                return
        else:
            if not os.path.isdir(self.labelPathEdit.text()):
                QMessageBox.warning(self, "警告", "您选择的标签文件夹不存在")
                return

        if os.path.abspath("dataset").startswith(os.path.abspath(self.imagePathEdit.text())):
            QMessageBox.warning(self, "警告",
                                "您不能选择该文件夹作为图片文件夹，因为它在复制时会引起递归拷贝。")
            return
        if os.path.abspath("dataset").startswith(os.path.abspath(self.labelPathEdit.text())) and self.config.type_ == 'yolo':
            QMessageBox.warning(self, "警告",
                                "您不能选择该文件夹作为标签文件夹，因为它在复制时会引起递归拷贝。")
            return
        if self.config.name == self.nameEdit.text() and \
                self.config.image_path == self.imagePathEdit.text() and \
                self.config.label_path == self.labelPathEdit.text():
            QMessageBox.information(self, "提示", "您没有修改任何信息，不需要更新")
            return

        dialog = CommonDialog(self, "确认操作", "您确定要更新信息吗？")
        if dialog.exec_() == dialog.Accepted:
            self.config.name = self.nameEdit.text()
            self.config.image_path = self.imagePathEdit.text()
            self.config.label_path = self.labelPathEdit.text()
            self.master.update_dataset_info(self.config)

    @Slot()
    def on_deleteDatasetButton_clicked(self):
        dialog = DeleteDatasetDialog(self.config, self)
        if dialog.exec_() == dialog.Accepted:
            self.master.delete_dataset(self.config)
            self.hide()

    @Slot()
    def on_cleanDatasetButton_clicked(self):
        dialog = CommonDialog(self, "清理数据集", "您确认要清理数据集吗？",
                              "清理数据集会清理没有任何标签的图片信息，以及没有任何标签的类别。\n"
                              "清理一般情况下不会造成数据集的任何问题")
        if dialog.exec_() == dialog.Accepted:
            clean(self.config.label_path)

    @Slot()
    def on_copyDatasetButton_clicked(self):
        dialog = CopyDatasetDialog(self.config, self)
        if dialog.exec_() == dialog.Accepted:
            self.master.add_dataset(dialog.new_config)

    @Slot()
    def on_exportButton_clicked(self):
        dialog = ArchiveDatasetDialog(self.config, self)
        dialog.exec_()

    @Slot()
    def on_divideButton_clicked(self):
        dialog = DivideDatasetDialog(self.config, self)
        dialog.exec_()

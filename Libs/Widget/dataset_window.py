import os.path

from ..Ui.ui_dataset_window import Ui_Form
from .common_dialog import CommonDialog
from .delete_dataset_dialog import DeleteDatasetDialog
from ..Dataset import clean_coco
from .. import dataset_config
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
        if config.data_type == dataset_config.DataType.TRAIN:
            self.dataTypeLabel.setText(f"{config.type_} 格式的训练集")
        elif config.data_type == dataset_config.DataType.VAL:
            self.dataTypeLabel.setText(f"{config.type_} 格式的验证集")
        else:
            self.dataTypeLabel.setText(f"{config.type_} 格式的数据集")
        if config.type_ != 'coco':
            self.cleanDatasetButton.setVisible(False)
        else:
            self.cleanDatasetButton.setVisible(True)
        if config.data_type in (dataset_config.DataType.TRAIN, dataset_config.DataType.VAL):
            self.divideButton.setEnabled(False)
            self.divideButton.setToolTip("该数据集已经是训练/验证集，无法再划分")

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
            if self.config.parent is not None:
                self.master.delete_dataset(self.config.parent.train)
                self.master.delete_dataset(self.config.parent.val)
            else:
                self.master.delete_dataset(self.config)
            self.hide()

    @Slot()
    def on_cleanDatasetButton_clicked(self):
        result = clean_coco.check_coco(self.config.label_path)
        if result:
            dialog = CommonDialog(self, "清理数据集", "数据集中存在如下问题",
                                  "\n".join(result) + "\n是否要清理数据集？",
                                  ("清理", "返回"))
            if dialog.exec_() == dialog.Rejected:
                return
            else:
                clean_coco.clean(self.config.label_path)
        else:
            QMessageBox.information(self, "提示", "数据集中没有任何问题，不需要清理")

    @Slot()
    def on_copyDatasetButton_clicked(self):
        dialog = CopyDatasetDialog(self.config, self)
        if dialog.exec_() == dialog.Accepted:
            if dialog.new_config.data_type != dataset_config.DataType.MERGED:
                self.master.add_dataset(dialog.new_config)
            else:
                self.master.add_dataset(dialog.new_config.train)
                self.master.add_dataset(dialog.new_config.val)

    @Slot()
    def on_exportButton_clicked(self):
        dialog = ArchiveDatasetDialog(self.config, self)
        dialog.exec_()

    @Slot()
    def on_divideButton_clicked(self):
        dialog = DivideDatasetDialog(self.config, self)
        dialog.exec_()

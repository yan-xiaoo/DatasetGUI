import os
import shutil

from ..Ui.ui_add_dataset_dialog import Ui_Dialog
from .common_dialog import CommonDialog
from ..work_functions import CopyDir
from ..process_window import ProcessWindow
from .. import dataset_config
from ..Dataset import clean_coco
from ..changelog import ChangeLog
from PySide2.QtWidgets import QDialog, QFileDialog, QMessageBox
from PySide2.QtCore import Slot


class AddDatasetDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.on_currentIndexChanged(0)
        self.config = None

        self.datasetTypeBox.currentIndexChanged.connect(self.on_currentIndexChanged)
        self.singleButton.clicked.connect(self.single_multiple_clicked)
        self.multipleButton.clicked.connect(self.single_multiple_clicked)
        self.cocoMergeEdit.textEdited.connect(self.cocoMergeEdit_textEdited)
        self.yoloMergeEdit.textEdited.connect(self.yoloMergeEdit_textEdited)

    @Slot()
    def on_currentIndexChanged(self, index):
        if index == 0 and self.singleButton.isChecked():
            self.yoloBox.setVisible(False)
            self.cocoMergeFrame.setVisible(False)
            self.yoloMergeFrame.setVisible(False)
            self.cocoBox.setVisible(True)
            self.checkDatasetBox.setVisible(True)
            self.cleanDatasetBox.setVisible(True)
            self.adjustSize()
        elif index == 0 and self.multipleButton.isChecked():
            self.yoloBox.setVisible(False)
            self.cocoBox.setVisible(False)
            self.cocoMergeFrame.setVisible(True)
            self.yoloMergeFrame.setVisible(False)
            self.checkDatasetBox.setVisible(True)
            self.cleanDatasetBox.setVisible(True)
            self.adjustSize()
        elif index == 1 and self.singleButton.isChecked():
            self.yoloBox.setVisible(True)
            self.cocoBox.setVisible(False)
            self.cocoMergeFrame.setVisible(False)
            self.yoloMergeFrame.setVisible(False)
            self.checkDatasetBox.setVisible(False)
            self.cleanDatasetBox.setVisible(False)
            self.adjustSize()
        else:
            self.yoloBox.setVisible(False)
            self.cocoBox.setVisible(False)
            self.cocoMergeFrame.setVisible(False)
            self.yoloMergeFrame.setVisible(True)
            self.checkDatasetBox.setVisible(False)
            self.cleanDatasetBox.setVisible(False)
            self.adjustSize()

    @Slot()
    def single_multiple_clicked(self):
        self.on_currentIndexChanged(index=self.datasetTypeBox.currentIndex())

    @Slot()
    def on_cocoImageButton_clicked(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec_():
            self.cocoImageEdit.setText(dialog.selectedFiles()[0])
            if not self.cocoName.text():
                self.cocoName.setText(os.path.basename(dialog.selectedFiles()[0]))

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
            if not self.yoloName.text():
                self.yoloName.setText(os.path.basename(dialog.selectedFiles()[0]))

    @Slot()
    def on_yoloLabelButton_clicked(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec_():
            self.yoloLabelEdit.setText(dialog.selectedFiles()[0])

    @Slot()
    def on_cocoTrainImageButton_clicked(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec_():
            self.cocoTrainImageEdit.setText(dialog.selectedFiles()[0])

    @Slot()
    def on_cocoTrainLabelButton_clicked(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilters(["Json Files(*.json)", "All files(*.*)"])
        if dialog.exec_():
            self.cocoTrainLabelEdit.setText(dialog.selectedFiles()[0])

    @Slot()
    def on_cocoValImageButton_clicked(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec_():
            self.cocoValImageEdit.setText(dialog.selectedFiles()[0])

    @Slot()
    def on_cocoValLabelButton_clicked(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilters(["Json Files(*.json)", "All files(*.*)"])
        if dialog.exec_():
            self.cocoValLabelEdit.setText(dialog.selectedFiles()[0])

    @Slot()
    def cocoMergeEdit_textEdited(self, text):
        self.cocoTrainEdit.setText(text + '_训练')
        self.cocoValEdit.setText(text + '_验证')

    @Slot()
    def on_yoloTrainImageButton_clicked(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec_():
            self.yoloTrainImageEdit.setText(dialog.selectedFiles()[0])

    @Slot()
    def on_yoloTrainLabelButton_clicked(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec_():
            self.yoloTrainLabelEdit.setText(dialog.selectedFiles()[0])

    @Slot()
    def on_yoloValImageButton_clicked(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec_():
            self.yoloValImageEdit.setText(dialog.selectedFiles()[0])

    @Slot()
    def on_yoloValLabelButton_clicked(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        if dialog.exec_():
            self.yoloValLabelEdit.setText(dialog.selectedFiles()[0])

    @Slot()
    def yoloMergeEdit_textEdited(self, text):
        self.yoloTrainEdit.setText(text + '_训练')
        self.yoloValEdit.setText(text + '_验证')

    @Slot()
    def on_okButton_clicked(self):
        if self.datasetTypeBox.currentIndex() == 0:
            type_ = 'coco'
        else:
            type_ = 'yolo'

        if self.singleButton.isChecked():
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
                if os.path.abspath("dataset").startswith(self.cocoImageEdit.text()) and self.copyDatasetBox.checkState():
                    QMessageBox.warning(self, "警告",
                                        "您不能选择该文件夹作为图片文件夹，因为它会引起递归拷贝。取消勾选“拷贝数据集”后，您可以选择该文件夹")
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
                if os.path.abspath("dataset").startswith(self.yoloImageEdit.text()) and self.copyDatasetBox.checkState():
                    QMessageBox.warning(self, "警告",
                                        "您不能选择该文件夹作为图片文件夹，因为它会引起递归拷贝。取消勾选“拷贝数据集”后，您可以选择该文件夹")
                    return
                if os.path.abspath("dataset").startswith(self.yoloLabelEdit.text()) and self.copyDatasetBox.checkState():
                    QMessageBox.warning(self, "警告",
                                        "您不能选择该文件夹作为标签文件夹，因为它会引起递归拷贝。取消勾选“拷贝数据集”后，您可以选择该文件夹")
                    return

            if self.copyDatasetBox.checkState():
                pass
            else:
                warn = CommonDialog(self, "警告", "删除该数据集时存在安全隐患",
                                    "如果您不复制该数据集，则删除该数据集时，无法同时删除数据集文件\n"
                                    "这是因为，我们无法确定数据集中哪部分是真正的数据，哪部分是您的文件\n"
                                    "直接删除的话，您的数据很可能被误删\n"
                                    "您可以点击“返回”并勾选“拷贝数据集”来解决这个问题\n", ("仍然继续", "返回"))
                warn.cancelButton.setFocus()
                if warn.exec_() == warn.Accepted:
                    pass
                else:
                    return

            if self.checkDatasetBox.checkState() and type_ == 'coco' and not self.cleanDatasetBox.checkState():
                try:
                    result = clean_coco.check_coco(self.cocoLabelEdit.text())
                except AssertionError:
                    QMessageBox.warning(self, "警告", "您选择的标签文件不是一个合法的COCO标签文件")
                    return
                if result:
                    dialog = CommonDialog(self, "警告", "数据集中存在问题",
                                          "您可以选择“返回”并勾选清理数据集来解决一部分问题\n" +
                                          "\n".join(clean_coco.check_coco(self.cocoLabelEdit.text())),
                                          ("继续", "返回"))
                    if dialog.exec_() == dialog.Rejected:
                        return

            if self.copyDatasetBox.checkState():
                if type_ == 'coco':
                    d = dataset_config.get_available_id()
                    thread = CopyDir(self.cocoImageEdit.text(), f"dataset/{d}/images", d, "正在复制数据集图片")
                    window = ProcessWindow(thread, self, title="复制数据集", stoppable=True)
                    result = window.exec_()
                    if result == window.Rejected:
                        return
                    log = ChangeLog.load(d)
                    log.append(os.path.abspath(f"dataset/{d}/dataset.json"))
                    shutil.copyfile(self.cocoLabelEdit.text(), f"dataset/{d}/dataset.json")
                    log.save(d)
                    self.config = dataset_config.DatasetConfig.from_type("coco", {"name": self.cocoName.text(),
                                                                                  "image_path": f"dataset/{d}/images",
                                                                                  "label_path": f"dataset/{d}/dataset.json"})
                elif type_ == 'yolo':
                    d = dataset_config.get_available_id()
                    thread = CopyDir(self.yoloImageEdit.text(), f"dataset/{d}/images", d, "正在复制数据集图片")
                    window = ProcessWindow(thread, self, title="复制数据集", stoppable=True)
                    if window.exec_() == window.Rejected:
                        return
                    thread = CopyDir(self.yoloLabelEdit.text(), f"dataset/{d}/labels", d, "正在复制数据集标签")
                    window = ProcessWindow(thread, self, title="复制数据集", stoppable=True)
                    if window.exec_() == window.Rejected:
                        return
                    self.config = dataset_config.DatasetConfig.from_type("yolo", {"name": self.yoloName.text(),
                                                                                  "image_path": f"dataset/{d}/images",
                                                                                  "label_path": f"dataset/{d}/labels"})
            else:
                self.config = dataset_config.DatasetConfig.from_type(type_, {
                    "name": self.cocoName.text() if type_ == 'coco' else self.yoloName.text(),
                    "image_path": self.cocoImageEdit.text() if type_ == 'coco' else self.yoloImageEdit.text(),
                    "label_path": self.cocoLabelEdit.text() if type_ == 'coco' else self.yoloLabelEdit.text()})

            if self.cleanDatasetBox.checkState() and type_ == 'coco':
                clean_coco.clean(self.config.label_path)

            self.accept()
        else:
            pass

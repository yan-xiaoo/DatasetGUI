from ..Ui.ui_archive_dataset_dialog import Ui_Dialog
from PySide2.QtWidgets import QDialog, QFileDialog, QMessageBox
from PySide2.QtGui import QDesktopServices
from PySide2.QtCore import Slot, QUrl
from .common_dialog import CommonDialog
from ..process_window import ProcessWindow, ProcessFunction
import os
import tarfile
import zipfile


class ArchiveDatasetDialog(QDialog, Ui_Dialog):
    def __init__(self, config, parent=None):
        super().__init__(parent)
        self.config = config
        self.setupUi(self)
        self.nameEdit.setText(self.config.name)
        self.outputEdit.setText(os.path.abspath("export"))

    @Slot()
    def on_outputButton_clicked(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(dialog.Directory)
        if dialog.exec_():
            self.outputEdit.setText(dialog.selectedFiles()[0])

    @Slot()
    def on_okButton_clicked(self):
        if not os.path.isdir("export") and self.outputEdit.text() == os.path.abspath("export"):
            os.mkdir("export")
        if not self.nameEdit.text():
            QMessageBox.warning(self, "警告", "请您为导出文件命名")
        if not self.outputEdit.text():
            QMessageBox.warning(self, "警告", "请您选择导出路径")
        if not os.path.isdir(self.outputEdit.text()):
            QMessageBox.warning(self, "警告", "您选择的导出位置不存在或不是文件夹")
        if os.path.dirname(self.config.label_path) == os.path.dirname(self.config.image_path):
            together = True
        else:
            together = False

        if together:
            if self.zipButton.isChecked():
                result = self.achieve_dataset_zip(os.path.join(self.outputEdit.text(), self.nameEdit.text() + '.zip'),
                                                  os.path.dirname(self.config.image_path),
                                                  except_ds_store=self.ignoreBox.checkState(),
                                                  hint="正在压缩数据集")
                if result == self.Rejected:
                    return
            else:
                result = self.achieve_dataset(os.path.join(self.outputEdit.text(), self.nameEdit.text() + '.tar.gz'),
                                              os.path.dirname(self.config.image_path),
                                              except_ds_store=self.ignoreBox.checkState(),
                                              hint="正在压缩数据集")
                if result == self.Rejected:
                    return
        else:
            if self.zipButton.isChecked():
                if self.config.type_ == 'coco':
                    result = self.achieve_dataset_zip(
                        os.path.join(self.outputEdit.text(), self.nameEdit.text() + '.zip'),
                        self.config.image_path, except_ds_store=self.ignoreBox.checkState(),
                        hint="正在压缩数据集", additional_file=self.config.label_path)
                    if result == ProcessWindow.Rejected:
                        return
                else:
                    result = self.achieve_dataset_zip(
                        os.path.join(self.outputEdit.text(), self.nameEdit.text() + '_image.zip'),
                        self.config.image_path, except_ds_store=self.ignoreBox.checkState(), hint="正在压缩数据集图片")
                    if result == ProcessWindow.Rejected:
                        return
                    result = self.achieve_dataset_zip(
                        os.path.join(self.outputEdit.text(), self.nameEdit.text() + '_label.zip'),
                        self.config.label_path, except_ds_store=self.ignoreBox.checkState(), hint="正在压缩数据集标签")
                    if result == ProcessWindow.Rejected:
                        return
            else:
                if self.config.type_ == "coco":
                    result = self.achieve_dataset(
                        os.path.join(self.outputEdit.text(), self.nameEdit.text() + '.tar.gz'),
                        self.config.image_path, except_ds_store=self.ignoreBox.checkState(),
                        hint="正在压缩数据集", additional_file=self.config.label_path)
                    if result == ProcessWindow.Rejected:
                        return
                else:
                    result = self.achieve_dataset(
                        os.path.join(self.outputEdit.text(), self.nameEdit.text() + '_image.tar.gz'),
                        self.config.image_path, except_ds_store=self.ignoreBox.checkState(), hint="正在压缩数据集图片")
                    if result == ProcessWindow.Rejected:
                        return
                    result = self.achieve_dataset(
                        os.path.join(self.outputEdit.text(), self.nameEdit.text() + '_label.tar.gz'),
                        self.config.label_path, except_ds_store=self.ignoreBox.checkState(), hint="正在压缩数据集标签")
                    if result == ProcessWindow.Rejected:
                        return

        desktop = QDesktopServices()
        desktop.openUrl(QUrl.fromLocalFile(self.outputEdit.text()))
        self.accept()

    def achieve_dataset(self, output_name, src_dir, except_ds_store=False, hint="正在压缩数据集", additional_file=None):
        if os.path.exists(output_name):
            dialog = CommonDialog(self, title="文件已存在", text="导出目标位置已存在同名文件",
                                  detail_text=f"您是否要覆盖已存在的文件\n {output_name} ？",
                                  button_texts=["覆盖", "取消"])
            if dialog.exec_() == dialog.Rejected:
                return dialog.Rejected
        thread = ArchiveDataset(output_name, src_dir, except_ds_store=except_ds_store, hint=hint,
                                additional_file=additional_file)
        processWindow = ProcessWindow(thread, title="正在压缩并导出数据集", stoppable=True)
        return processWindow.exec_()

    def achieve_dataset_zip(self, output_name, src_dir, except_ds_store=False, hint="正在压缩数据集文件",
                            additional_file=None):
        if os.path.exists(output_name):
            dialog = CommonDialog(self, title="文件已存在", text="导出目标位置已存在同名文件",
                                  detail_text=f"您是否要覆盖已存在的文件\n {output_name} ？",
                                  button_texts=["覆盖", "取消"])
            if dialog.exec_() == dialog.Rejected:
                return dialog.Rejected
        thread = ArchiveDatasetZip(output_name, src_dir, except_ds_store=except_ds_store, hint=hint,
                                   additional_file=additional_file)
        processWindow = ProcessWindow(thread, title="正在压缩并导出数据集", stoppable=True)
        return processWindow.exec_()


class ArchiveDataset(ProcessFunction):
    def __init__(self, output_filename, source_dir, except_ds_store=False, hint="正在压缩数据集", additional_file=None):
        super().__init__()
        self.output_filename = output_filename
        self.source_dir = source_dir
        self.except_ds_store = except_ds_store
        self.hint = hint
        self.additional_file = additional_file

    def run(self):
        self.setText.emit(self.hint)
        with tarfile.open(self.output_filename, "w:gz") as tar:
            for root, dirs, files in os.walk(self.source_dir):
                self.setMaximum.emit(len(files))
                for i in range(len(files)):
                    if self.except_ds_store and files[i] == '.DS_Store':
                        print(f"忽略了.DS_Store文件 {os.path.join(root, files[i])}")
                        continue
                    pathfile = os.path.join(root, files[i])
                    tar.add(pathfile, os.path.relpath(pathfile, self.source_dir))
                    self.setDetailedText.emit("正在添加文件： " + pathfile)
                    self.setProgress.emit(i)
                    if not self.can_run:
                        tar.close()
                        os.remove(self.output_filename)
                        self.stopped.emit()
                        return
            if self.additional_file is not None:
                tar.add(self.additional_file, os.path.basename(self.additional_file))
            tar.close()
            self.has_finished.emit()


class ArchiveDatasetZip(ProcessFunction):
    def __init__(self, output_filename, source_directory, except_ds_store=False, hint="正在压缩数据集",
                 additional_file=None):
        super().__init__()
        self.output_filename = output_filename
        self.source_directory = source_directory
        self.except_ds_store = except_ds_store
        self.hint = hint
        self.additional_file = additional_file

    def run(self):
        self.setText.emit(self.hint)
        with zipfile.ZipFile(self.output_filename, "w", zipfile.ZIP_DEFLATED) as zip_file:
            for root, dirs, files in os.walk(self.source_directory):
                self.setMaximum.emit(len(files))
                for i in range(len(files)):
                    if self.except_ds_store and files[i] == '.DS_Store':
                        print(f"忽略了.DS_Store文件 {os.path.join(root, files[i])}")
                        continue
                    pathfile = os.path.join(root, files[i])
                    zip_file.write(pathfile, os.path.relpath(pathfile, self.source_directory))
                    self.setDetailedText.emit("正在添加文件： " + pathfile)
                    self.setProgress.emit(i)
                    if not self.can_run:
                        zip_file.close()
                        os.remove(self.output_filename)
                        self.stopped.emit()
                        return
            if self.additional_file is not None:
                zip_file.write(self.additional_file, os.path.basename(self.additional_file))
            zip_file.close()
            self.has_finished.emit()

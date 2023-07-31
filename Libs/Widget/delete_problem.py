from ..Ui.ui_delete_problem import Ui_Dialog
from .common_dialog import CommonDialog
from PySide2.QtWidgets import QDialog, QMessageBox
from PySide2.QtCore import QUrl, Slot
from PySide2.QtGui import QDesktopServices
import os


class DeleteProblemDialog(QDialog, Ui_Dialog):
    def __init__(self, config, parent=None):
        super().__init__(parent)
        self.config = config
        self.setupUi(self)

    @Slot()
    def on_imageButton_clicked(self):
        service = QDesktopServices()
        service.openUrl(QUrl.fromLocalFile(self.config.image_path))

    @Slot()
    def on_labelButton_clicked(self):
        service = QDesktopServices()
        if self.config.type_ == 'coco':
            QMessageBox.information(self, "提示", "您的标签文件是该文件夹下的 {}".format(os.path.basename(self.config.label_path)))
            service.openUrl(QUrl.fromLocalFile(os.path.dirname(self.config.label_path)))
        elif self.config.type_ == 'yolo':
            service.openUrl(QUrl.fromLocalFile(self.config.label_path))

    @Slot()
    def on_whyButton_clicked(self):
        dialog = CommonDialog(self, "惨痛的经历",
                              "为什么不能删除工作目录以外的数据集文件？",
                              "曾经，本程序使用shutil.rmtree()函数删除数据集文件夹，这个函数大概相当于rm -rf\n"
                              "会删除一个目录和它的所有子目录，且无法找回\n"
                              "在一次测试中，开发者不小心把数据集图片路径填成了脚本自己的位置，结果测试删除时删光了整个程序和所有数据\n"
                              "因此，现在重写的程序会在创建数据集时记录哪些文件是被复制来的，可以删除\n"
                              "但工作目录外的文件没经过复制，程序不知道它们是不是数据集的文件，所以不能删除\n",
                              ["我知道了", "返回"])
        dialog.exec_()

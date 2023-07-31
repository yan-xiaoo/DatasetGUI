from ..Ui.ui_delete_dataset_dialog import Ui_Dialog
from PySide2.QtWidgets import QDialog
from PySide2.QtCore import Slot
from .common_dialog import CommonDialog
from .delete_problem import DeleteProblemDialog
from ..dataset_config import get_id_by_config
from ..work_functions import ClearDir
from ..process_window import ProcessWindow


class DeleteDatasetDialog(QDialog, Ui_Dialog):
    def __init__(self, config, parent=None):
        super().__init__(parent)
        self.config = config
        self.setupUi(self)
        self.textLabel.setText("确定要删除名为 {} 的数据集吗？".format(config.name))

    @Slot()
    def on_okButton_clicked(self):
        if get_id_by_config(self.config) is not None:
            if self.clearFileBox.checkState():
                dialog = CommonDialog(self, "删除警告", "您确定要同时删除数据集的文件吗",
                                      "这将会删除数据集的所有图片和标签文件，且永远无法恢复",
                                      ["删除", "取消"])
                if dialog.exec_() == QDialog.Rejected:
                    return
                else:
                    thread = ClearDir(get_id_by_config(self.config), "正在清除数据集数据")
                    window = ProcessWindow(thread, self, stoppable=False)
                    window.exec_()
                    self.accept()
            else:
                self.accept()
        else:
            if self.clearFileBox.checkState():
                dialog = DeleteProblemDialog(self.config, self)
                dialog.exec_()
                return
            else:
                self.accept()

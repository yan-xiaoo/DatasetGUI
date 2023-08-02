from ..Ui.ui_divide_dataset_dialog import Ui_Dialog
from PySide2.QtWidgets import QDialog, QMessageBox
from PySide2.QtCore import Slot
from .common_dialog import CommonDialog


class DivideDatasetDialog(QDialog, Ui_Dialog):
    def __init__(self, config, parent=None):
        super().__init__(parent)
        self.config = config
        self.setupUi(self)
        self.trainEdit.setText(self.config.name + "_训练")
        self.valEdit.setText(self.config.name + "_验证")
        self.trainBox.valueChanged.connect(self.trainBox_valueChanged)
        self.valBox.valueChanged.connect(self.valBox_valueChanged)

    @Slot()
    def trainBox_valueChanged(self, value):
        self.valBox.setValue(100 - value)

    @Slot()
    def valBox_valueChanged(self, value):
        self.trainBox.setValue(100 - value)

    @Slot()
    def on_okButton_clicked(self):
        if not self.trainEdit.text():
            QMessageBox.warning(self, "警告", "请您为新的训练集起名")
            return
        if not self.valEdit.text():
            QMessageBox.warning(self, "警告", "请您为新的验证集起名")
            return

        if self.onedirButton.isChecked():
            dialog = CommonDialog(self, "删除时的问题", "删除时两数据集会被一同删除",
                                  "如果您选择将训练集与验证集存放在同一目录下，\n"
                                  "则删除一个数据集的文件时会同时删除另一个的文件\n"
                                  "如果您能接受该问题，请点击“接受”以继续", ["接受", "返回"])
            if dialog.exec_() == dialog.Rejected:
                return

        self.accept()

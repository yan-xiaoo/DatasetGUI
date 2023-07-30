from ..Ui.ui_add_dataset_dialog import Ui_Dialog
from PySide2.QtWidgets import QDialog
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


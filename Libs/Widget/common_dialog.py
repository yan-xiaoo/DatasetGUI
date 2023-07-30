from ..Ui.ui_common_dialog import Ui_Dialog
from PySide2.QtWidgets import QDialog


class CommonDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None, title=None, text=None, detail_text=None):
        super().__init__(parent)
        self.setupUi(self)

        if title is not None:
            self.setWindowTitle(title)
        if text is not None:
            self.textLabel.setText(text)
        if detail_text is not None:
            self.detailTextLabel.setText(text)

    def setText(self, text):
        self.textLabel.setText(text)

    def setDetailedText(self, text):
        self.detailTextLabel.setText(text)

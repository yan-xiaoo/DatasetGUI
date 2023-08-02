from ..Ui.ui_common_dialog import Ui_Dialog
from PySide2.QtWidgets import QDialog


class CommonDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None, title=None, text=None, detail_text=None, button_texts=None):
        super().__init__(parent)
        self.setupUi(self)

        if title is not None:
            self.setWindowTitle(title)
        if text is not None:
            self.textLabel.setText(text)
        if detail_text is not None:
            self.detailTextLabel.setText(detail_text)
        else:
            self.detailTextLabel.setVisible(False)
        if button_texts is not None:
            self.okButton.setText(button_texts[0])
            self.cancelButton.setText(button_texts[1])
        self.adjustSize()

    def setText(self, text):
        self.textLabel.setText(text)
        self.adjustSize()

    def setDetailedText(self, text):
        if text:
            self.detailTextLabel.setText(text)
            self.detailTextLabel.setVisible(True)
        else:
            self.detailTextLabel.setVisible(False)
        self.adjustSize()

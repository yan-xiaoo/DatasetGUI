from ..Ui.ui_check_result_dialog import Ui_Dialog
from PySide2.QtWidgets import QDialog, QMessageBox
from PySide2.QtCore import Slot


class CheckResultDialog(QDialog, Ui_Dialog):
    def __init__(self, problems, expand=None, parent=None, clean_slot=None):
        super().__init__(parent)
        self.setupUi(self)

        self.clean_func = clean_slot
        if clean_slot is None:
            self.cleanButton.setVisible(False)
            self.numberLabel.setText(f"数据集中存在 {len(problems)} 项问题")
        else:
            self.numberLabel.setText(f"数据集中存在 {len(problems)} 项问题，点击“执行清理”按钮清理数据集")

        if expand is None:
            if len(problems) >= 5:
                expand = True
            else:
                expand = False
        if expand:
            self.detailLabel.setText("点击“展开”查看详细内容")
            for problem in problems:
                self.problemList.addItem(problem)
            self.problemList.setVisible(False)
        else:
            self.expandButton.setVisible(False)
            self.problemList.setVisible(False)
            self.detailLabel.setText("\n".join(problems))

        self.problems = problems
        self.adjustSize()

    @Slot()
    def on_expandButton_clicked(self):
        if self.problemList.isVisible():
            self.expandButton.setText("展开")
            self.problemList.setVisible(False)
            self.adjustSize()
        else:
            self.expandButton.setText("收起")
            self.problemList.setVisible(True)
            self.adjustSize()

    @Slot()
    def on_cleanButton_clicked(self):
        if self.clean_func is not None:
            self.clean_func()
            QMessageBox.information(self, "清理完成", "数据集已经清理完成")
            self.accept()

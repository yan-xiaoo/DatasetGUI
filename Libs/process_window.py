from PySide2.QtCore import QThread, Slot, Signal, QTimer
from PySide2.QtWidgets import QDialog
from .Ui.ui_process_window import Ui_Dialog


class ProcessFunction(QThread):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.can_run = True

    setText = Signal(str)
    setDetailedText = Signal(str)
    has_finished = Signal()
    stopped = Signal()
    setProgress = Signal(int)
    setRange = Signal(int, int)
    setMaximum = Signal(int)

    @Slot()
    def stopProcess(self):
        self.can_run = False


class ProcessWindow(QDialog, Ui_Dialog):
    def __init__(self, work_function: ProcessFunction, parent=None, title=None, text=None, detailed_text=None,
                 stoppable=False):
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowTitle(title)
        self.Text.setText(text)
        self.detailedText.setText(detailed_text)
        if not stoppable:
            self.stopButton.setEnabled(False)

        self.work_function = work_function
        self.time_out_timer = QTimer()
        self.time_out_timer.setInterval(1000)
        self.time_out_timer.timeout.connect(self.check_process)

        self.stopChildProcess.connect(self.work_function.stopProcess)
        self.work_function.setText.connect(self.setText)
        self.work_function.setDetailedText.connect(self.setDetailedText)
        self.work_function.has_finished.connect(self.finishProcess)
        self.work_function.stopped.connect(self.stopProcess)
        self.work_function.setProgress.connect(self.setProgress)
        self.work_function.setRange.connect(self.setRange)
        self.work_function.setMaximum.connect(self.setMaximum)

    def exec_(self) -> int:
        self.work_function.start()
        return super().exec_()

    stopChildProcess = Signal()

    @Slot()
    def setText(self, text):
        self.Text.setText(text)

    @Slot()
    def setDetailedText(self, text):
        self.detailedText.setText(text)

    @Slot()
    def setProgress(self, value):
        self.progressBar.setValue(value)

    @Slot()
    def setRange(self, minium, maximum):
        self.progressBar.setRange(minium, maximum)

    @Slot()
    def setMaximum(self, value):
        self.progressBar.setMaximum(value)

    @Slot()
    def finishProcess(self):
        self.work_function.wait()
        self.accept()

    @Slot()
    def stopProcess(self):
        self.work_function.wait()
        self.reject()

    @Slot()
    def check_process(self):
        if not self.work_function.isRunning():
            self.time_out_timer.stop()
            self.reject()

    @Slot()
    def on_stopButton_clicked(self):
        self.stopButton.setEnabled(False)
        self.setWindowTitle(self.windowTitle() + "[等待子进程退出]")
        self.stopChildProcess.emit()
        self.time_out_timer.start()
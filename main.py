from PySide2.QtWidgets import QApplication
from Libs.Widget.main_window import MainWindow
import os


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    app = QApplication()
    window = MainWindow()
    window.show()
    try:
        app.exec_()
    finally:
        window.dataset_manager.save("dataset/config.json")

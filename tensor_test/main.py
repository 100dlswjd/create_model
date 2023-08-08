import sys

from ui.main_form import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_model_create.setEnabled(False)
        self.pushButton_model_create.clicked.connect(self.btn_model_create_handler)
        self.pushButton_select_csv_file_path.clicked.connect(self.btn_select_csv_file_path_handler)

    def btn_model_create_handler(self):
        pass

    def btn_select_csv_file_path_handler(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
import sys
import pandas as pd
import copy

from ui.main_form import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_model_create.setEnabled(False)
        self.pushButton_model_create.clicked.connect(self.btn_model_create_handler)
        self.pushButton_select_csv_file_path.clicked.connect(self.btn_select_csv_file_path_handler)
        self.comboBox.currentTextChanged.connect(self.comboBox_currentTextChanged_handler)        

    def comboBox_currentTextChanged_handler(self):
        select_column =  self.comboBox.currentText()
        full_columns = copy.deepcopy(self.columns)
        full_columns.remove(select_column)
        self.label_colum_list.setText(str(full_columns))
        pass

    def btn_model_create_handler(self):
        pass

    def btn_select_csv_file_path_handler(self):
        file_path = QFileDialog.getOpenFileName(self, "Select CSV File", "", "CSV Files (*.csv)")
        if file_path:
            file_path = file_path[0]
            self.label_file_path.setText(file_path)
            self.pushButton_model_create.setEnabled(True)
            self.comboBox.setEnabled(True)

            data = pd.read_csv(file_path)
            self.columns = data.columns
            self.columns = list(self.columns)
            self.comboBox.clear()
            for idx in self.columns:
                self.comboBox.addItem(idx)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.setStyle('Fusion')
    window.show()
    app.exec()
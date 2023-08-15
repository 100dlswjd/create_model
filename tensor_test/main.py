import sys
import pandas as pd
import copy

import pandas as pd
import tensorflow as tf

from ui.main_form import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.file_path = ""
        self.pushButton_model_create.setEnabled(False)
        self.pushButton_model_create.clicked.connect(self.btn_model_create_handler)
        self.pushButton_select_csv_file_path.clicked.connect(self.btn_select_csv_file_path_handler)
        self.comboBox.currentTextChanged.connect(self.comboBox_currentTextChanged_handler)        

    def comboBox_currentTextChanged_handler(self):
        select_column =  self.comboBox.currentText()
        full_columns = copy.deepcopy(self.columns)
        full_columns.remove(select_column)
        self.label_colum_list.setText(str(full_columns))

    def btn_model_create_handler(self):
        df = pd.read_csv(self.file_path)

        target = df[self.comboBox.currentText()]
        feature = df.drop(self.comboBox.currentText(), axis=1)        

        X = tf.keras.layers.Input(shape=[feature.columns.size])
        H = tf.keras.layers.Dense(10, activation='swish')(X)
        y = tf.keras.layers.Dense(1)(H)

        model = tf.keras.models.Model(X, y)
        model.compile(loss='mse')

        H = tf.keras.layers.Dense(4, activation='swish')(X)
        H1 = tf.keras.layers.Dense(4, activation='swish')(H)
        y = tf.keras.layers.Dense(1)(H1)

        # 모델 학습 및 저장
        model.fit(feature, target, epochs=1000, verbose=0)
        model.save('model.h5')


    def btn_select_csv_file_path_handler(self):
        file_path = QFileDialog.getOpenFileName(self, "Select CSV File", "", "CSV Files (*.csv)")
        if file_path:
            file_path = file_path[0]
            self.label_file_path.setText(file_path)
            self.file_path = file_path
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
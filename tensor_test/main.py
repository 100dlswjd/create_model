import sys
import pandas as pd
import copy


from ui.main_form import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.csv_file_path = ""
        self.save_file_path = ""
        self.pushButton_model_create.setEnabled(False)
        self.pushButton_model_create.clicked.connect(self.btn_model_create_handler)
        self.pushButton_select_csv_file_path.clicked.connect(self.btn_select_csv_file_path_handler)
        self.comboBox.currentTextChanged.connect(self.comboBox_currentTextChanged_handler)        
        self.pushButton_save_path.clicked.connect(self.btn_save_path_handler)

    def btn_save_path_handler(self):
        file_name = QFileDialog.getSaveFileName(self, "Save File", "", "H5 Files (*.h5)")
        if file_name[0]:
            self.save_file_path = file_name[0]
            self.label_save_path.setText(file_name[0])
            self.pushButton_model_create.setEnabled(True)
        else:
            self.save_file_path = ""
            self.label_save_path.setText("")
            self.pushButton_model_create.setEnabled(False)

    def comboBox_currentTextChanged_handler(self):
        select_column =  self.comboBox.currentText()
        full_columns = copy.deepcopy(self.columns)
        full_columns.remove(select_column)
        self.label_colum_list.setText(str(full_columns))

    def btn_model_create_handler(self):
        import pandas as pd
        import tensorflow as tf
        self.pushButton_model_create.setEnabled(False)
        self.pushButton_model_create.setText("모델 생성 중")
        df = pd.read_csv(self.csv_file_path)

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
        model.save(self.save_file_path)        
        self.pushButton_model_create.setText("모델 생성 완료")

    def btn_select_csv_file_path_handler(self):
        file_path = QFileDialog.getOpenFileName(self, "Select CSV File", "", "CSV Files (*.csv)")
        if file_path[0]:
            self.comboBox.clear()
            file_path = file_path[0]
            self.label_file_path.setText(file_path)
            self.csv_file_path = file_path

            self.comboBox.setEnabled(True)
            self.pushButton_save_path.setEnabled(True)

            data = pd.read_csv(file_path)
            self.columns = data.columns
            self.columns = list(self.columns)
            
            for idx in self.columns:
                self.comboBox.addItem(idx)
        else:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.setStyle('Fusion')
    window.show()
    app.exec()
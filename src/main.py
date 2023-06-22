import os
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Signal, Slot

from ui.main_form import Ui_MainWindow
from ui.class_tab_form import Ui_class_tab

from threading import Thread

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator

class ClassTab(QMainWindow, Ui_class_tab):
    def __init__(self, class_name : str):
        super().__init__()
        self.setupUi(self)
        self.class_name = class_name
        self.label_class_name.setText(class_name)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tab_list = list()
        self.pushButton_add_class.clicked.connect(self.btn_add_class_tab_handler)
        self.lineEdit_class_name.returnPressed.connect(self.btn_add_class_tab_handler)
        self.pushButton_delete_class.clicked.connect(self.btn_delete_class_tab_handler)
        self.pushButton_make.clicked.connect(self.btn_make_handler)
    
    @Slot()
    def btn_add_class_tab_handler(self) -> bool:
        if not self.lineEdit_class_name.text():
            return False
        name = self.lineEdit_class_name.text()
        tab = ClassTab(name)
        self.tab_list.append(tab)
        self.tabWidget.addTab(tab, name)
        self.lineEdit_class_name.setText("")
        if self.tabWidget.count() > 0:
            self.pushButton_make.setEnabled(True)
        return True

    @Slot()
    def btn_delete_class_tab_handler(self) -> bool:
        if self.tabWidget.count() == 0:
            return False
        index = self.tabWidget.currentIndex()
        del self.tab_list[index]
        self.tabWidget.removeTab(index)
        return True
    
    def work_thread(self, classes_dir_list : list):
        for dir_path in classes_dir_list:
            train_names = os.listdir(dir_path)
            print(train_names)
        
        pass

    @Slot()
    def btn_make_handler(self):
        work_thread = Thread(target=self.work_thread, args=(self.tab_list,))
        work_thread.start()
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
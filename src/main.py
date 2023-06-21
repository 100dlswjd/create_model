import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Signal, Slot

from ui.main_form import Ui_MainWindow
from ui.class_tab_form import Ui_class_tab

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
        self.pushButton_add_class.clicked.connect(self.btn_add_class_tab_handler)
        self.lineEdit_class_name.returnPressed.connect(self.btn_add_class_tab_handler)
        self.pushButton_delete_class.clicked.connect(self.btn_delete_class_tab_handler)
    
    def btn_add_class_tab_handler(self) -> bool:
        if not self.lineEdit_class_name.text():
            return False
        name = self.lineEdit_class_name.text()
        self.tabWidget.addTab(ClassTab(name), name)
        self.lineEdit_class_name.setText("")
        return True

    def btn_delete_class_tab_handler(self) -> bool:
        if self.tabWidget.count() == 0:
            return False
        
        self.tabWidget.removeTab(self.tabWidget.currentIndex())
        return True

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
import os
import sys
import shutil
import random

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import Signal, Slot

from ui.main_form import Ui_MainWindow
from ui.class_tab_form import Ui_class_tab

from threading import Thread

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import tensorflow as tf
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator

class ClassTab(QMainWindow, Ui_class_tab):
    def __init__(self, class_name : str):
        super().__init__()
        self.setupUi(self)
        self.class_name = class_name
        self.dir_path = ""
        self.label_class_name.setText(class_name)
        self.pushButton_select_folder.clicked.connect(self.btn_select_folder_handler)

    def btn_select_folder_handler(self):
        file = QFileDialog.getExistingDirectory(self, "Select Directory")
        if file:
            self.lineEdit_select_folder_path.setText(file)
            self.dir_path = file

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
    
    def work_thread(self, class_dir_list : list):
        def mkdir(path : str) -> bool:
            if not os.path.isdir(path):
                os.mkdir(path)
                return True
            else:
                shutil.rmtree(path)
                os.mkdir(path)
                return True

        def create_model(train_dir_path : str, validation_dir_path : str, test_dir_path : str, model_name : str = "model.h5"):
            from tensorflow.keras.preprocessing import image
            from tensorflow.keras.preprocessing.image import ImageDataGenerator
            
            train_datagen = ImageDataGenerator(rescale = 1./255,
                                            rotation_range=25,
                                            width_shift_range=0.05,
                                            height_shift_range=0.05,
                                            zoom_range=0.2,
                                            horizontal_flip=True,
                                            vertical_flip=True,
                                            fill_mode='nearest'
                                            ) 
            
            validation_datagen = ImageDataGenerator(rescale = 1./255)
            test_datagen = ImageDataGenerator(rescale = 1./255) 

            train_generator = train_datagen.flow_from_directory(train_dir_path, 
                                                                batch_size=16, # 한번에 변환된 이미지 16개씩 만들어라 라는 것
                                                                color_mode='grayscale', # 흑백 이미지 처리
                                                                class_mode='binary', 
                                                                target_size=(150,150)) # target_size에 맞춰서 이미지의 크기가 조절된다
            validation_generator = validation_datagen.flow_from_directory(validation_dir_path, 
                                                                        batch_size=4, 
                                                                        color_mode='grayscale',
                                                                        class_mode='binary', 
                                                                        target_size=(150,150))
            test_generator = test_datagen.flow_from_directory(test_dir_path,
                                                            batch_size=4,
                                                            color_mode='grayscale',
                                                            class_mode='binary',
                                                            target_size=(150,150))
            
            train_generator.class_indices

            import tensorflow as tf

            model = tf.keras.models.Sequential([
                tf.keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(150, 150, 1)),
                tf.keras.layers.MaxPooling2D(2,2),
                tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
                tf.keras.layers.MaxPooling2D(2,2),
                tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
                tf.keras.layers.MaxPooling2D(2,2),
                tf.keras.layers.Flatten(),
                tf.keras.layers.Dense(512, activation='relu'),
                tf.keras.layers.Dense(1, activation='sigmoid')
            ])
            model.summary()

            from tensorflow.keras.optimizers import RMSprop
            
            model.compile(optimizer=RMSprop(learning_rate=0.001),
                        loss='binary_crossentropy',
                        metrics= ["accuracy"])
            
            model.fit_generator(train_generator,
                                validation_data=validation_generator,
                                steps_per_epoch=4,
                                epochs=100, 
                                validation_steps=4,
                                verbose=2)
            
            model.evaluate(train_generator) 

            model.save(model_name)


        train_dir = "train"
        validation_dir = "validation"
        test_dir = "test"

        mkdir(train_dir)
        mkdir(validation_dir)
        mkdir(test_dir)
        
        class_name_list = list()
        # 폴더생성
        for class_dir in class_dir_list:
            tem_train_dir = os.path.join(train_dir, class_dir.class_name)
            mkdir(tem_train_dir)
            tem_validation_dir = os.path.join(validation_dir, class_dir.class_name)
            mkdir(tem_validation_dir)
            tem_test_dir = os.path.join(test_dir, class_dir.class_name)
            mkdir(tem_test_dir)
            class_name_list.append(class_dir.class_name)
            
        
        # 이미지 이동
        for class_dir in class_dir_list:
            class_dir : ClassTab = class_dir
            for file in os.listdir(class_dir.dir_path):
                if random.random() < 0.7:
                    shutil.copy(os.path.join(class_dir.dir_path, file), os.path.join(train_dir, class_dir.class_name))
                else:
                    shutil.copy(os.path.join(class_dir.dir_path, file), os.path.join(validation_dir, class_dir.class_name))

        # 모델 생성
        create_model(train_dir, validation_dir, test_dir)

        with open("label.txt", "w", encoding='utf-8') as f:
            index = 0
            for class_name in class_name_list:
                f.write(str(index) + " " + class_name + "\n")
                index += 1
        

    @Slot()
    def btn_make_handler(self):
        work_thread = Thread(target=self.work_thread, args=(self.tab_list,))
        work_thread.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
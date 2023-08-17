# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(414, 247)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.label_file_path = QLabel(self.centralwidget)
        self.label_file_path.setObjectName(u"label_file_path")
        self.label_file_path.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_file_path)

        self.pushButton_select_csv_file_path = QPushButton(self.centralwidget)
        self.pushButton_select_csv_file_path.setObjectName(u"pushButton_select_csv_file_path")

        self.horizontalLayout.addWidget(self.pushButton_select_csv_file_path)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.label_target = QLabel(self.centralwidget)
        self.label_target.setObjectName(u"label_target")
        self.label_target.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_target)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(4, 4, 4, 4)
        self.label_columns = QLabel(self.centralwidget)
        self.label_columns.setObjectName(u"label_columns")

        self.horizontalLayout_5.addWidget(self.label_columns)

        self.label_colum_list = QLabel(self.centralwidget)
        self.label_colum_list.setObjectName(u"label_colum_list")

        self.horizontalLayout_5.addWidget(self.label_colum_list)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(4, 4, 4, 4)
        self.label_save_path = QLabel(self.centralwidget)
        self.label_save_path.setObjectName(u"label_save_path")

        self.horizontalLayout_6.addWidget(self.label_save_path)

        self.pushButton_save_path = QPushButton(self.centralwidget)
        self.pushButton_save_path.setObjectName(u"pushButton_save_path")
        self.pushButton_save_path.setEnabled(False)

        self.horizontalLayout_6.addWidget(self.pushButton_save_path)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.pushButton_model_create = QPushButton(self.centralwidget)
        self.pushButton_model_create.setObjectName(u"pushButton_model_create")
        self.pushButton_model_create.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.pushButton_model_create)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 414, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\ubaa8\ub378 \uc0c8\uc131", None))
        self.label_file_path.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c", None))
        self.pushButton_select_csv_file_path.setText(QCoreApplication.translate("MainWindow", u"csv \ud30c\uc77c \uc120\ud0dd", None))
        self.label_target.setText(QCoreApplication.translate("MainWindow", u"\ud0c0\uac9f", None))
        self.label_columns.setText(QCoreApplication.translate("MainWindow", u"columns : ", None))
        self.label_colum_list.setText("")
        self.label_save_path.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5\uc704\uce58", None))
        self.pushButton_save_path.setText(QCoreApplication.translate("MainWindow", u"\ucc3e\uae30", None))
        self.pushButton_model_create.setText(QCoreApplication.translate("MainWindow", u"model_create", None))
    # retranslateUi


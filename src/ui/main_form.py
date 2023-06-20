# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(327, 251)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.label_class_name = QLabel(self.centralwidget)
        self.label_class_name.setObjectName(u"label_class_name")

        self.horizontalLayout.addWidget(self.label_class_name)

        self.lineEdit_class_name = QLineEdit(self.centralwidget)
        self.lineEdit_class_name.setObjectName(u"lineEdit_class_name")

        self.horizontalLayout.addWidget(self.lineEdit_class_name)

        self.pushButton_add_class = QPushButton(self.centralwidget)
        self.pushButton_add_class.setObjectName(u"pushButton_add_class")

        self.horizontalLayout.addWidget(self.pushButton_add_class)

        self.pushButton_delete_class = QPushButton(self.centralwidget)
        self.pushButton_delete_class.setObjectName(u"pushButton_delete_class")

        self.horizontalLayout.addWidget(self.pushButton_delete_class)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")

        self.horizontalLayout_2.addWidget(self.tabWidget)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 327, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\ubd84\ub958 \ubaa8\ub378 \ub9cc\ub4e4\uae30", None))
        self.label_class_name.setText(QCoreApplication.translate("MainWindow", u"\ud074\ub798\uc2a4 \uc774\ub984", None))
        self.pushButton_add_class.setText(QCoreApplication.translate("MainWindow", u"\ud074\ub798\uc2a4 \ucd94\uac00", None))
        self.pushButton_delete_class.setText(QCoreApplication.translate("MainWindow", u"\ud074\ub799\uc2a4 \uc0ad\uc81c", None))
    # retranslateUi


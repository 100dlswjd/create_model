# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'class_tab_form.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_class_tab(object):
    def setupUi(self, class_tab):
        if not class_tab.objectName():
            class_tab.setObjectName(u"class_tab")
        class_tab.resize(331, 126)
        class_tab.setMinimumSize(QSize(331, 126))
        self.horizontalLayout_4 = QHBoxLayout(class_tab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.label_class_name = QLabel(class_tab)
        self.label_class_name.setObjectName(u"label_class_name")

        self.horizontalLayout_3.addWidget(self.label_class_name)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.label_dir_path = QLabel(class_tab)
        self.label_dir_path.setObjectName(u"label_dir_path")

        self.horizontalLayout.addWidget(self.label_dir_path)

        self.lineEdit_select_folder_path = QLineEdit(class_tab)
        self.lineEdit_select_folder_path.setObjectName(u"lineEdit_select_folder_path")
        self.lineEdit_select_folder_path.setEnabled(False)

        self.horizontalLayout.addWidget(self.lineEdit_select_folder_path)

        self.pushButton_select_folder = QPushButton(class_tab)
        self.pushButton_select_folder.setObjectName(u"pushButton_select_folder")

        self.horizontalLayout.addWidget(self.pushButton_select_folder)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.label = QLabel(class_tab)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout)


        self.retranslateUi(class_tab)

        QMetaObject.connectSlotsByName(class_tab)
    # setupUi

    def retranslateUi(self, class_tab):
        class_tab.setWindowTitle(QCoreApplication.translate("class_tab", u"class_tab_form", None))
        self.label_class_name.setText(QCoreApplication.translate("class_tab", u"class_name", None))
        self.label_dir_path.setText(QCoreApplication.translate("class_tab", u"\ud3f4\ub354 \uacbd\ub85c", None))
        self.pushButton_select_folder.setText(QCoreApplication.translate("class_tab", u"\ud3f4\ub354 \uc120\ud0dd", None))
        self.label.setText(QCoreApplication.translate("class_tab", u"\u203b \uc120\ud0dd\ud55c \ud3f4\ub354 \uc548\uc5d0\ub294 \uc774\ubbf8\uc9c0 \ud30c\uc77c\ub9cc \uc874\uc7ac\ud574\uc57c \ud569\ub2c8\ub2e4.", None))
    # retranslateUi


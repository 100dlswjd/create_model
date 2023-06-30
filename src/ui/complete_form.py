# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'complete_form.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Complete(object):
    def setupUi(self, Complete):
        if not Complete.objectName():
            Complete.setObjectName(u"Complete")
        Complete.resize(128, 92)
        self.horizontalLayout_3 = QHBoxLayout(Complete)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.label_complete = QLabel(Complete)
        self.label_complete.setObjectName(u"label_complete")
        self.label_complete.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_complete)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_acept = QPushButton(Complete)
        self.pushButton_acept.setObjectName(u"pushButton_acept")

        self.horizontalLayout_2.addWidget(self.pushButton_acept)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(Complete)

        QMetaObject.connectSlotsByName(Complete)
    # setupUi

    def retranslateUi(self, Complete):
        Complete.setWindowTitle(QCoreApplication.translate("Complete", u"\uc54c\ub9bc", None))
        self.label_complete.setText(QCoreApplication.translate("Complete", u"\ubcc0\ud658\uc644\ub8cc", None))
        self.pushButton_acept.setText(QCoreApplication.translate("Complete", u"\ud655\uc778", None))
    # retranslateUi


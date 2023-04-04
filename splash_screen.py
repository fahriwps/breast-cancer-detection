# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screengSeOzb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *


class Ui_SplashScreen(object):
    """Base class for Splash Screen UI."""

    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(680, 400)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName("dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(
            "QFrame{\n"
            "	\n"
            "	background-color: rgb(39, 39, 39);\n"
            "	color: rgb(220, 220, 220);\n"
            "	border-radius: 20px;\n"
            "}\n"
            ""
        )
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName("label_title")
        self.label_title.setGeometry(QRect(0, 80, 661, 111))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(20, 167, 108);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.dropShadowFrame)
        self.label_description.setObjectName("label_description")
        self.label_description.setGeometry(QRect(0, 180, 661, 31))
        font1 = QFont()
        font1.setFamily("Segoe UI")
        font1.setPointSize(14)
        self.label_description.setFont(font1)
        self.label_description.setStyleSheet("color: rgb(128, 128, 128);")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setGeometry(QRect(70, 240, 500, 23))
        self.progressBar.setStyleSheet("QProgressBar {\n" "\n" "}")
        self.progressBar.setValue(24)
        self.label_credit = QLabel(self.dropShadowFrame)
        self.label_credit.setObjectName("label_credit")
        self.label_credit.setGeometry(QRect(20, 340, 621, 31))
        font1 = QFont()
        font1.setFamily("Segoe UI")
        font1.setPointSize(6)
        self.label_credit.setFont(font1)
        self.label_credit.setStyleSheet("color: rgb(255, 250, 250);")
        self.label_credit.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )
        self.label_loading = QLabel(self.dropShadowFrame)
        self.label_loading.setObjectName("label_loading")
        self.label_loading.setGeometry(QRect(0, 270, 661, 31))
        font2 = QFont()
        font2.setFamily("Segoe UI")
        font2.setPointSize(12)
        self.label_loading.setFont(font2)
        self.label_loading.setStyleSheet("color: rgb(255, 250, 250);")
        self.label_loading.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(
            QCoreApplication.translate("SplashScreen", "MainWindow", None)
        )
        self.label_title.setText(
            QCoreApplication.translate(
                "SplashScreen", "<strong>Neural</strong>SIGHT", None
            )
        )
        self.label_description.setText(
            QCoreApplication.translate(
                "SplashScreen",
                '<html><head/><body><p><span style=" font-size:14pt;">Breast Cancer Early Detection System</span></p></body></html>',
                None,
            )
        )
        self.label_credit.setText(
            QCoreApplication.translate(
                "SplashScreen",
                '<html><head/><body><p><span style=" font-size:9pt; font-weight:600;">Created:</span><span style=" font-size:9pt;"> NeuralSIGHT Team</span></p></body></html>',
                None,
            )
        )
        self.label_loading.setText(
            QCoreApplication.translate(
                "SplashScreen",
                '<html><head/><body><p><span style=" font-size:12pt;">Please Wait</span></p></body></html>',
                None,
            )
        )

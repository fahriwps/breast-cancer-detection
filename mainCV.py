################################################################################
## 
## Created by: fahriwps
## Compile this file as chmod -x run.py
## Run this file as ./run.py
################################################################################

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

# SPLASH SCREEN
from splash_screen import Ui_SplashScreen

# MAIN WINDOW
from main_windowCV import Ui_MainWindow

# GLOBALS
counter = 0

# MAIN WINDOW CLASS
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.center()

    def center(self):
        setGeometry = self.frameGeometry()
        centerGeometry = QDesktopWidget().availableGeometry().center()
        setGeometry.moveCenter(centerGeometry)
        self.move(setGeometry.topLeft())

# SPLASH SCREEN CLASS
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        # DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        # QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(45)

        # Initial Text
        self.ui.label_description.setText("Breast Cancer Early Detection")
        self.ui.label_loading.setText("Please Wait")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_loading.setText("Loading Assets"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_loading.setText("Loading User Interface"))

        self.center()
        self.show()

    # APP FUNCTIONS
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREEN AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1

    def center(self):
        setGeometry = self.frameGeometry()
        centerGeometry = QDesktopWidget().availableGeometry().center()
        setGeometry.moveCenter(centerGeometry)
        self.move(setGeometry.topLeft())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())

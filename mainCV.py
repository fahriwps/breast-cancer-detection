################################################################################
##
## Created by: NeuralSIGHT Team
## Give execution permission to this file with chmod -x mainCV.py
## Run this file as ./mainCV.py
################################################################################

import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *
from splash_screen import Ui_SplashScreen
from main_windowCV import Ui_MainWindow

counter = 0


class MainWindow(QMainWindow):
    """Main Class responsible for handling main window."""

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.center()

    def center(self):
        """Set main window to center position."""
        setGeometry = self.frameGeometry()
        centerGeometry = QDesktopWidget().availableGeometry().center()
        setGeometry.moveCenter(centerGeometry)
        self.move(setGeometry.topLeft())


class SplashScreen(QMainWindow):
    def __init__(self):
        """Class resposible for handling splash screen effect
        before loading main window.
        """

        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(45)  # Timer in milisecond
        self.ui.label_description.setText("Breast Cancer Early Detection System")
        self.ui.label_loading.setText("Please Wait")
        QtCore.QTimer.singleShot(
            1500, lambda: self.ui.label_loading.setText("Loading Assets")
        )
        QtCore.QTimer.singleShot(
            3000, lambda: self.ui.label_loading.setText("Loading User Interface")
        )
        self.center()
        self.show()

    def progress(self):
        """Splash screen progress bar functionality."""
        global counter
        self.ui.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop()
            self.main = MainWindow()
            self.main.show()
            self.close()

        counter += 1

    def center(self):
        """Set splash screen to center position."""
        setGeometry = self.frameGeometry()
        centerGeometry = QDesktopWidget().availableGeometry().center()
        setGeometry.moveCenter(centerGeometry)
        self.move(setGeometry.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())

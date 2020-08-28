import sys
import os
import subprocess
import gui_window
from PyQt5 import QtCore, QtGui, QtWidgets

# Compile this file as chmod -x run.py
# Run this file as ./run.py

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) 
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

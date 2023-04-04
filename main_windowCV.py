################################################################################
##
## Created by: NeuralSIGHT Team
##
################################################################################

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QImage
from PyQt5.QtCore import QCoreApplication
import cv2

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:

    def _fromUtf8(s):
        return s


try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)

except AttributeError:

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    """Base class for Main Window UI."""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1900, 900)
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        MainWindow.setStyleSheet(
            "QFrame {\n" "	\n" "	background-color: rgb(220, 220, 220)\n" "}"
        )
        # self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 941, 671))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(7)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(960, 50, 931, 671))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setLineWidth(7)
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(210, 740, 591, 31))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QtCore.QRect(350, 10, 281, 31))
        font3 = QtGui.QFont()
        font3.setFamily("Segoe UI")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_3.setFont(font3)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QtCore.QRect(1330, 10, 281, 31))
        self.label_4.setFont(font3)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)

        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(30, 740, 161, 31))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.browse_file)

        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(1100, 740, 771, 91))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(self.predict)
        self.pushButton_3.setIcon(QIcon("search.png"))

        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(246, 0))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.save_predict)
        self.pushButton.setIcon(QIcon("save.png"))

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1900, 25))
        self.menubar.setObjectName("menubar")

        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NeuralSIGHT"))
        self.pushButton_2.setText(_translate("MainWindow", "Browse File"))
        self.pushButton_3.setText(_translate("MainWindow", "PREDICT"))
        self.pushButton.setText(_translate("MainWindow", "SAVE FILE"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.label_3.setText(QCoreApplication.translate("MainWindow", "INPUT", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", "OUTPUT", None))

    def browse_file(self):
        """Browse button functionality to open new image."""
        self.directory, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "Browse File", "", "Image File (*.png *.PNG *.jpg *.JPG)"
        )
        self.label.setPixmap(QtGui.QPixmap(self.directory))
        self.label.setScaledContents(True)
        self.lineEdit.setText("{}".format(self.directory))

    def save_predict(self):
        """Save button functionality to save inference image."""
        savePredict, _ = QtWidgets.QFileDialog.getSaveFileName(
            None, "Save Predict", "", "Image File (*.png *.PNG *.jpg *.JPG)"
        )
        pixmap2 = self.label_2.pixmap()
        pixmap2.save(savePredict)

    def draw_bboxs(self, img, classes, confidences, boxes, names):
        for class_id, confidence, box in zip(
            classes.flatten(), confidences.flatten(), boxes
        ):
            label = "%.2f" % confidence
            label = "%s: %s" % (names[class_id], label)
            label_size, base_line = cv2.getTextSize(
                label, cv2.FONT_HERSHEY_SIMPLEX, 1.5, 1
            )
            left, top, width, height = box
            top = max(top, label_size[1])
            cv2.rectangle(img, box, color=(0, 255, 0), thickness=3)
            cv2.rectangle(
                img,
                (left, top - label_size[1]),
                (left + label_size[0], top + base_line),
                (255, 255, 255),
                cv2.FILLED,
            )
            cv2.putText(
                img, label, (left, top), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2
            )

    def predict(self):
        """Main inference function responsible for predicting image."""
        obj_names = "data/obj.names"
        with open(obj_names, "r") as file:
            names = file.read().rstrip("\n").split("\n")

        cfg = "data/yolov4-obj.cfg"
        with open(cfg, "r") as f:
            lines = f.readlines()
            lines = [line.strip() for line in lines]

        width = list(filter(lambda x: "width" in x, lines))[0]
        width = int(width.split("=", 1)[-1])
        height = list(filter(lambda x: "height" in x, lines))[0]
        height = int(height.split("=", 1)[-1])

        weights = "weights/yolov4-obj_final.weights"
        confidence = 0.25
        nms = 0.45

        net = cv2.dnn_DetectionModel(cfg, weights)
        net.setInputSize(width=width, height=height)
        net.setInputScale(1.0 / 255.0)
        net.setInputSwapRB(True)

        self.input_image = cv2.imread(self.directory, -1)
        classes, confidences, boxes = net.detect(
            self.input_image, confThreshold=confidence, nmsThreshold=nms
        )
        self.output_image = self.input_image.copy()
        if not isinstance(classes, tuple):
            self.draw_bboxs(self.output_image, classes, confidences, boxes, names)
        self.output_image = QImage(
            self.output_image.data,
            self.output_image.shape[1],
            self.output_image.shape[0],
            QtGui.QImage.Format_RGB888,
        ).rgbSwapped()
        self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.output_image))
        self.label_2.setScaledContents(True)

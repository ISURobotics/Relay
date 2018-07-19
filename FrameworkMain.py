import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from pydispatch import dispatcher
import cv2
import time, threading
from OpenCV_Camera import Camera
from HSV_Transform import HSV_Transform
from Threshold_HSV import Threshold_HSV

CAMSENDER = 'camsender'
CAMSIG = 'An Image'
HSVSIG = 'An HSV Image'


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn = QPushButton("Quit", self)
        btn.clicked.connect(QApplication.instance().quit)
        btn.setToolTip("This is a <b>QPushButton</b> widget")
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        txt = QLineEdit(self)
        txt.move(50, 100)

        cmb = QComboBox(self)
        cmb.addItems(["Battlebot", "Exo", "Snowplow"])
        cmb.move(50, 150)

        self.resize(720, 480)
        self.move(300, 300)
        self.setWindowTitle("Framework - ISU Robotics Club")
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure you want to quit?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    print("Relay beginning...")
    camera_thread = threading.Thread(target=Camera, args=(1280, 720, 0, 0, True)) #Params = width, height, cameraID, SENSOROUTPUTID, visualizeBoolean
    camera_thread.start()
    hsv_thread = threading.Thread(target=HSV_Transform, args=(0, 1, True)) #Params = inputSensorID, outputSensorID, visualizeBoolean
    hsv_thread.start()
    thresh_thread = threading.Thread(target=Threshold_HSV, args=(1, 2, 15, 15, 15, 100, 100, 200, True)) #Params = inputSensorID, outputSensorID, hsvLOW, hsvHigh, visualizeBoolean
    thresh_thread.start()

    # app = QApplication(sys.argv)
    # ex = Example()
    #
    # sys.exit(app.exec_())

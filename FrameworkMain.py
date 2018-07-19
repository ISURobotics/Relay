import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from pydispatch import dispatcher
import cv2
import time, threading

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


class CameraSender():
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.run()

    def getImage(self):
        return self.cap.read()[1]

    def sendImg(self):
        dispatcher.send(message=self.getImage(), signal=CAMSIG, sender=CAMSENDER)

    def run(self):
        while True:
            self.sendImg()


class ImageReceive():
    def __init__(self):
        dispatcher.connect(self.dispatcher_receive, signal=CAMSIG, sender=CAMSENDER)
        self.run()

    def dispatcher_receive(self, message):
        print("Received an image")
        cv2.imshow("Message", message)
        cv2.waitKey(1)

    def run(self):
        while (True):
            continue


class HSVTransform():
    def __init__(self):
        dispatcher.connect(self.dispatcher_receive, signal=CAMSIG, sender=CAMSENDER)
        self.run()

    def dispatcher_receive(self, message):
        print("HSV TIME!")
        self.hsv = cv2.cvtColor(message, cv2.COLOR_BGR2HSV)
        cv2.imshow("HSV", self.hsv)
        cv2.waitKey(1)
        dispatcher.send(message=self.hsv, signal=HSVSIG, sender=CAMSENDER)

    def run(self):
        while True:
            continue

class ThreshHSV():
    def __init__(self):
        dispatcher.connect(self.dispatcher_receive, signal=HSVSIG, sender=CAMSENDER)
        self.run()

    def dispatcher_receive(self, message):
        self.thresh = cv2.inRange(message, (20, 20, 20), (100, 100, 100))
        cv2.imshow("Thresholded Image", self.thresh)
        cv2.waitKey(1)

    def run(self):
        while True:
            continue


if __name__ == '__main__':
    print("Running main")
    sender_thread = threading.Thread(target=CameraSender)
    sender_thread.start()
    hsv_thread = threading.Thread(target=HSVTransform)
    hsv_thread.start()
    rec_thread = threading.Thread(target=ImageReceive)
    rec_thread.start()
    thresh_thread = threading.Thread(target=ThreshHSV)
    thresh_thread.start()


    # app = QApplication(sys.argv)
    # ex = Example()
    #
    # sys.exit(app.exec_())

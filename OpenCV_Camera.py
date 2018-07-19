import cv2
from pydispatch import dispatcher
import time, threading

class Camera():
    def __init__(self, width, height, cameraID, sensorID, visualize=False):
        self.cap = cv2.VideoCapture(cameraID)
        self.cap.set(3, width)
        self.cap.set(4, height)
        self.sensorID = sensorID
        self.visualize = visualize
        self.img = None
        self.run()

    def getImage(self):
        self.img = self.cap.read()[1]
        if self.visualize:
            cv2.imshow("Camera", self.img)
            cv2.waitKey(1)
        return self.img

    def sendImg(self):
        dispatcher.send(message=self.getImage(), signal='image' + str(self.sensorID), sender='image')

    def run(self):
        while True:
            self.sendImg()
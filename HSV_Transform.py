import cv2
from pydispatch import dispatcher
import time, threading


class HSV_Transform():
    def __init__(self, inputID, outputID, visualize=False):
        self.type = 'image'
        self.signal = self.type + str(inputID)
        self.outsignal = self.type+str(outputID)
        self.visualize = visualize
        dispatcher.connect(self.dispatcher_receive, signal=self.signal, sender=self.type)
        self.run()

    def dispatcher_receive(self, message):
        self.hsv = cv2.cvtColor(message, cv2.COLOR_BGR2HSV)
        if self.visualize:
            cv2.imshow("HSV", self.hsv)
            cv2.waitKey(1)
        dispatcher.send(message=self.hsv, signal=self.outsignal, sender=self.type)

    def run(self):
        while True:
            continue

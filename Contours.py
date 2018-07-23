import cv2
import numpy as np
from pydispatch import dispatcher
import time, threading


class Find_Contours():
    def __init__(self, inputID, outputID, visualize=False):
        self.inType = 'image'
        self.outType = 'contours'
        self.signal = self.inType + str(inputID)
        self.outsignal = self.outType+str(outputID)
        self.visualize = visualize
        dispatcher.connect(self.dispatcher_receive, signal=self.signal, sender=self.inType)
        self.run()

    def dispatcher_receive(self, message):
        print("Received thresh")
        ret, tempthresh = cv2.threshold(message, 100, 255, cv2.THRESH_BINARY)
        image, contours, hierarchy = cv2.findContours(tempthresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        print("Found conts")
        cv2.drawContours(message, contours, -1,  255, 3)
        print("Drew contours")
        if self.visualize:
            cv2.imshow("Contours"+self.outsignal, message)
            cv2.waitKey(1)
        dispatcher.send(message=contours, signal=self.outsignal, sender=self.outType)

    def run(self):
        while True:
            continue

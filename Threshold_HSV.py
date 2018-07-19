import cv2
from pydispatch import dispatcher
import time, threading

class Threshold_HSV():
    def __init__(self, inputID, outputID, lowH, lowS, lowV, highH, highS, highV, visualize=False):
        self.type = 'image'
        self.lowBound = (lowH, lowS, lowV) #Passed individually for Cython
        self.highBound = (highH, highS, highV)
        self.signal = self.type + str(inputID)
        self.outsignal = self.type + str(outputID)
        self.visualize = visualize
        dispatcher.connect(self.dispatcher_receive, signal=self.signal, sender=self.type)
        self.run()

    def dispatcher_receive(self, message):
        self.thresh = cv2.inRange(message, self.lowBound, self.highBound)
        if self.visualize:
            cv2.imshow("Thresholded Image", self.thresh)
            cv2.waitKey(1)
        dispatcher.send(message=self.thresh, signal=self.outsignal, sender=self.type)

    def run(self):
        while True:
            continue
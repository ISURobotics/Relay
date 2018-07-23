import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from pydispatch import dispatcher
import cv2
import time, threading
import csv
from ast import literal_eval as make_tuple

#import all nodes
from OpenCV_Camera import Camera
from HSV_Transform import HSV_Transform
from Threshold_HSV import Threshold_HSV
from Contours import Find_Contours
importedItemDict = dict({'OpenCV_Camera': Camera, 'HSV_Transform': HSV_Transform, 'Threshold_HSV': Threshold_HSV, 'Contours': Find_Contours})


if __name__ == '__main__':
    print("Relay beginning...")

    #  Basic functionality is as follows:
    #  Each node has an input, output, or both.
    #  Camera has only an output, while HSV_Transform has an input and output
    #  Internally, each node (class) has a type.  For all OpenCV stuff, it's called 'image'
    #  All nodes also have an input signal ID and output signal ID
    #  To pass a message from one node to another, just match the input ID and output IDs
    #  See below for an example.
    #  Set the boolean for visualization of each thread.

    #Create a thread for each node

    #Camera node

    # camera_thread = threading.Thread(target=Camera, args=(1280, 720, 0, 0, True)) #Params = width, height, cameraID, SENSOROUTPUTID, visualizeBoolean
    # camera_thread.start()
    #
    # hsv_thread = threading.Thread(target=HSV_Transform, args=(0, 1, True)) #Params = inputSensorID, outputSensorID, visualizeBoolean
    # hsv_thread.start()
    #
    # thresh_thread = threading.Thread(target=Threshold_HSV, args=(1, 2, 15, 15, 0, 255, 255, 60, True)) #Params = inputSensorID, outputSensorID, hsvLOW, hsvHigh, visualizeBoolean
    # thresh_thread.start()
    #
    # #Another example thread showing how you can use a message in more than one receiving thread
    # rgb__thresh_thread = threading.Thread(target=Threshold_HSV, args = (0, 3, 15, 15, 0, 255, 255, 60, True))
    # rgb__thresh_thread.start()

    configfilename = r'C:\Users\xpist\Google Drive\College\Robotics\Relay\Config1.csv'
    with open(configfilename) as csvfile:
        reader = csv.DictReader(csvfile)
        threadList = []
        for row in reader:
            objName = row['Name']
            paramString = row['Parameters']
            params = make_tuple(paramString)
            objThread = threading.Thread(target=
                                         importedItemDict[objName], args=params)
            threadList.append(objThread)
        for thread in threadList:
            thread.start()




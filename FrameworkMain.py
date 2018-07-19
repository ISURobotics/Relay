import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from pydispatch import dispatcher
import cv2
import time, threading

#import all nodes
from OpenCV_Camera import Camera
from HSV_Transform import HSV_Transform
from Threshold_HSV import Threshold_HSV


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
    camera_thread = threading.Thread(target=Camera, args=(1280, 720, 0, 0, True)) #Params = width, height, cameraID, SENSOROUTPUTID, visualizeBoolean
    camera_thread.start()

    hsv_thread = threading.Thread(target=HSV_Transform, args=(0, 1, True)) #Params = inputSensorID, outputSensorID, visualizeBoolean
    hsv_thread.start()

    thresh_thread = threading.Thread(target=Threshold_HSV, args=(1, 2, 15, 15, 15, 100, 100, 200, True)) #Params = inputSensorID, outputSensorID, hsvLOW, hsvHigh, visualizeBoolean
    thresh_thread.start()

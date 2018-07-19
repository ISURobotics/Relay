# Overview
Framework for shared ISURC sensor communication.

# Description
Relay exists to ensure work done by members of ISURC is used and built upon for years to come.  Rather than letting code become obsolete when a member graduates, it will be "passed along" through this project.

Relay is a framework developed to let different sensors and devices communicate with each other, similar to ROS.  For example, in 2018 a member wrote a driver for a LiDAR.  The driver will eventually be maintained in this project, with a standardized way to access data created by the LiDAR.  That way, a new member can quickly and easily use the LiDAR in a future project by simply creating a new node that listens for LiDAR data.

The same concept may be applied to other sensors such as an IMU, an OpenCV camera, an encoder, etc.  Data created by these sensors will be interpreted by nodes created by members that follow a specific format (TBD).  For example, perhaps a new node may take the input from a Camera Node, process it and convert the image to a different color space, and publish a new image that another node can take advantage of.

# Installation
To use Relay, you must have Python 3.5 installed.  An Anaconda installation is recommended.  Because requirements to run Relay may change constantly, a requirements.txt file will be created (TO-DO) that allows a user to install multiple packages with pip all at once.  For now, pip install opencv-contrib-python, pip install pydispatcher, and pip install pyqt5 should do the trick.

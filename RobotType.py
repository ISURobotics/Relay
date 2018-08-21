from PositionType import Position
from pydispatch import dispatcher

class Robot():
    def __init__(self, inputID):
        self.inType = "Position"
        self.inSignal = self.inType + str(inputID)
        self.pose = Position()
        dispatcher.connect(self.dispatcher_receive, signal=self.signal, sender=self.inType)
        self.run()

    def dispatcher_receive(self, message):
        self.setPosition(message.x, message.y, message.z)
        self.printPose()

    def printPose(self):
       print("x, y, z, yaw: " + str(self.pose.x)  + ", " + str(self.pose.y) + ", " + str(self.pose.z) + ", " + str(self.pose.yaw))

    def setPosition(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def run(self):
        while True:
            continue
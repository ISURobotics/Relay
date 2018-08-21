from pydispatch import dispatcher
from PositionType import Position
import time
from random import uniform

class Generator():
    def __init__(self, outputID, dataPeriod = .1):
        self.outputID = outputID
        self.dataPeriod = .1
        self.outType = "Position"
        self.outsignal = self.outType + str(self.outputID)
        self.curPos = Position()
        self.run()
    def run(self):
        while True:
            self.curPos.x = uniform(-10, 10)
            self.curPos.y = uniform(-10, 10)
            self.curPos.z = uniform(-1, 1)
            dispatcher.send(message=self.curPos, signal=self.outsignal, sender=self.outType)
            time.sleep(self.dataPeriod)
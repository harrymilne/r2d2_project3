from random import randint

from PySide.QtGui import *
from PySide.QtCore import *

from robot import Robot
from treasure import *

class Field(QGraphicsScene):
    def __init__(self, x, y):
        super(Field, self).__init__()
        self.setSceneRect(0, 0, x, y)
        self.xy = (x, y)
        self.populate()
        self.robot = Robot(self)
        self.addItem(self.robot)
        self.robot.setPos(x/2-29, y/2-25)
        self.robot.orientate()

        print self.itemsBoundingRect()
        items = self.items()
        items.remove(self.robot)

        self.timer = QTimer()
        self.timer.timeout.connect(self.robot.process)
        self.timer.start(10)
        #QTimer.singleShot(5000, self.timer.stop)


    def populate(self):
        self.treasure = []
        existing = []

        for i in range(10):
            t = Treasure()
            self.treasure.append(t)
            self.addItem(t)
            rand_x = randint(50, self.xy[0]-50)
            rand_y = randint(50, self.xy[1]-50)
            t.setPos(rand_x, rand_y)
            if t.collidingItems():
                rand_x = randint(50, self.xy[0]-50)
                rand_y = randint(50, self.xy[1]-50)
                t.setPos(rand_x, rand_y)
        pass


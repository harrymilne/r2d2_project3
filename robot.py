from math import sqrt, pi, atan2, degrees

from PySide.QtGui import *
from PySide.QtCore import *

from treasure import TREASURE_TYPES

class Robot(QGraphicsPixmapItem):
    def __init__(self, scene):
        super(Robot, self).__init__()
        self.scene = scene
        self.picture = QPixmap("resources/robot.png")
        self.height = self.picture.height()
        self.width = self.picture.width()

        self.setPixmap(self.picture)
        self.setScale(0.5)
        self.setTransformOriginPoint(29, 25)

        self.items_found = []

    def get_nearest(self, items):
        #find closest
        h_list = []
        for i in items:
            l_x = abs(i.x() - self.x())
            l_y = abs(i.y() - self.y())
            h_list.append(sqrt(l_x**2 + l_y**2))
            print(h_list)
        max_h = min(h_list)
        closest_i = dict(zip(h_list, items))[max_h]
        return closest_i

    def orientate(self):
        items = self.scene.items()
        items.remove(self)
        print items
        item = self.get_nearest(items)
        x1, y1 = self.x(), self.y()
        x2, y2 = item.x(), item.y()
        dx = x2 - x1
        dy = y2 - y1

        self.current_target = (x2, y2)
        rads = atan2(dy, dx)
        deg = degrees(rads)
        self.setRotation(deg+90)

    def order_items(self):
        for passnum in range(len(self.items_found)-1,0,-1):
            for i in range(passnum):
                if TREASURE_TYPES[self.items_found[i].type]>TREASURE_TYPES[self.items_found[i+1].type]:
                    temp = self.items_found[i]
                    self.items_found[i] = self.items_found[i+1]
                    self.items_found[i+1] = temp
        print self.items_found

    def place_items(self):
        max_w = 800
        spacing = 100
        x = 50
        y = 50
        for i in self.items_found:
            self.scene.addItem(i)
            if x + spacing >= 800:
                x = 50
                y += spacing
            i.setPos(x, y)
            x += spacing

        

    def process(self):
        if len(self.scene.items()) > 1:
            items = self.collidingItems()
            if self.current_target[0] >= self.x():
                increment = 1
            elif self.current_target[0] < self.x():
                increment = -1
            dy = self.y() - self.current_target[1]
            dx = self.x() - self.current_target[0]
            if dx == 0:
                grad = 1
            else:
                grad = dy/dx
            if items:
                self.items_found.extend(items)
                for item in items:
                    self.scene.removeItem(item)
                self.orientate()
            else:
                self.moveBy(increment, grad*increment)

        else:
            self.order_items()
            self.place_items()
            self.scene.timer.stop()

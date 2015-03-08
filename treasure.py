from random import randint

from PySide.QtGui import *
from PySide.QtCore import *

TREASURE_TYPES = {"diamond":100, "emerald":80, "gold":60, "iron":40, "stick":20}

class Treasure(QGraphicsPixmapItem):
    def __init__(self):
        super(Treasure, self).__init__()


        self.type = TREASURE_TYPES.keys()[randint(0, len(TREASURE_TYPES)-1)]
        self.picture = QPixmap("resources/{}.png".format(self.type))
        self.height = self.picture.height()
        self.width = self.picture.width()
        self.setPixmap(self.picture)
        self.setScale(0.25)
        
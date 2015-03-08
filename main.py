import sys

from PySide.QtGui import *
from PySide.QtCore import *

from field import Field

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Treasure Finder")

        self.field = Field(800, 400)
        field_gv = QGraphicsView()
        field_gv.setScene(self.field)
        #field_gv.setFixedHeight(400)
        #field_gv.setFixedWidth(800)

        self.layout = QVBoxLayout()
        self.layout.addWidget(field_gv)
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)



app = QApplication(sys.argv)

dialog = MainWindow()
QPixmap()


dialog.show()
app.exec_()
sys.exit()

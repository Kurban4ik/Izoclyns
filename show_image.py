# -*- coding: utf-8 -*-

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QRadioButton, QApplication, QDialog, QLabel
from PyQt5.uic import loadUi
import sqlite3


class Example(QDialog):
    def __init__(self):
        super(Example, self).__init__()
        loadUi('image.ui', self)
        self.setFixedSize(500, 500)
        self.ok.clicked.connect(self.die)

    def load_image(self, file_name):
        self.pixmap = QPixmap(file_name)
        self.image.setPixmap(self.pixmap)
        self.image.resize(self.pixmap.width(), self.pixmap.height())

    def die(self):
        self.close()




if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = Example()
    w.load_image('amongus.png')
    w.show()
    sys.exit(app.exec_())

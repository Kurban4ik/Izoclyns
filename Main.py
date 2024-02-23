# -*- coding: utf-8 -*-
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from show_image import Example
from middle import draw_izo_PIL
import sys


class IzoSolution(QMainWindow):
    def __init__(self):
        super(IzoSolution, self).__init__()
        loadUi('main.ui', self)
        self.setWindowTitle('Постройка изоклин')
        self.ok.clicked.connect(self.draw_izo)

    def draw_izo(self):
        try:
            func = self.func.text()
            func = func.split('=')[1].replace(' ', '').replace('^', '**').replace('y`', 'y_p')
            dialog = Example()
            if self.fst_type.isChecked():
                w = draw_izo_PIL(100, func, 1, 20, 4).save('buf.png')
            else:
                draw_izo_PIL(100, func, 2, 20, 4).save('buf.png')
            dialog.load_image('buf.png')
            dialog.exec_()
            if not dialog.save_check.isChecked():
                os.remove('buf.png')

        except Exception as e:
            print(e)
            QMessageBox.critical(self, "Ошибка ", "Неправильно введена функция", QMessageBox.Ok)


def start():
    app = QApplication(sys.argv)
    w = IzoSolution()
    w.show()
    sys.exit(app.exec_())


start()

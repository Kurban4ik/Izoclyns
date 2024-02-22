import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from show_image import Example
from middle import draw_izo_PIL
import sys


class Game(QMainWindow):
    def __init__(self):
        super(Game, self).__init__()
        loadUi('main.ui', self)
        self.setWindowTitle('Постройка изоклин')
        self.ok.clicked.connect(self.draw_izo)

    def draw_izo(self):
        try:
            func = self.func.text()
            func = func.split('=')[1].replace(' ', '').replace('^', '**')
            dialog = Example()
            w = draw_izo_PIL(500, func)
            w.save('buffer.png')
            dialog.load_image('buffer.png')
            dialog.exec_()
            if not dialog.save_check.text() == 'Сохранить':
                os.remove('buffer.png')
        except Exception as e:
            print(e)
            QMessageBox.critical(self, "Ошибка ", "Неправильно введена функция", QMessageBox.Ok)


def start():
    app = QApplication(sys.argv)
    w = Game()
    w.show()
    sys.exit(app.exec_())


start()

import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QRadioButton
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
        if self.fst_type.isChecked():
            self.draw_izo_fst()
        elif self.scnd_type.isChecked():
            self.draw_izo_scnd()
    def draw_izo_fst(self):
        try:
            func = self.func.text()
            func = func.split('=')[1].replace(' ', '').replace('^', '**')
            dialog = Example()
            w = draw_izo_PIL(500, func)
            w.save('buffer.png')
            dialog.load_image('buffer.png')
            dialog.exec_()
            if not dialog.save_check.isChecked() == 'Сохранить':
                os.remove('buffer.png')

        except Exception as e:
            print(e)
            QMessageBox.critical(self, "Ошибка ", "Неправильно введена функция", QMessageBox.Ok)

    def draw_izo_scnd(self):
        pass

def start():
    app = QApplication(sys.argv)
    w = IzoSolution()
    w.show()
    sys.exit(app.exec_())


start()

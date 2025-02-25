import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
import api


currency = api.latest()


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('untitled.ui', self)

        self.btn.clicked.connect(self.convert)
        self.input_value.addItems(currency.keys())
        self.output_value.addItems(currency.keys())

    def convert(self):
        if self.input_box.text() != '':
            input = float(self.input_box.text()) / currency[self.input_value.currentText()]
            output = input * currency[self.output_value.currentText()]
            self.output_box.setText(f'{output: .2f}')
        else:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wind = Window()
    wind.show()
    sys.exit(app.exec())
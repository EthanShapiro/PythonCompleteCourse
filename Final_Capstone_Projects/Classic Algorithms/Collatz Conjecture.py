# Collatz Conjecture
# Start with a number n > 1
# if n is even, divide by 2
# if n is odd, multiply by 3 and add 1
# Do this until you get to 1

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QVBoxLayout, QWidget, QLabel
import pdb

class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()

        self.init_ui()
        self.setCentralWidget(self.main_widget)
        self.collatz_calculator = CollatzCalculator()

        self.setWindowTitle('Collatz Conjecture')
        self.setGeometry(250, 250, 400, 100)
        self.show()

    def init_ui(self):
        self.main_widget = QWidget()

        self.label_1 = QLabel('Please input a number')
        self.input_text = QLineEdit()
        input_button = QPushButton('Input Number')
        v_layout = QVBoxLayout()

        input_button.released.connect(self.callCalculator)

        v_layout.addWidget(self.label_1)
        v_layout.addWidget(self.input_text)
        v_layout.addWidget(input_button)
        self.main_widget.setLayout(v_layout)

    def callCalculator(self):
        if self.collatz_calculator.isValid(self.input_text.text()):
            num = int(self.input_text.text())
            collatz_num = self.collatz_calculator.num_recursions(num)
            self.label_1.setText(str(collatz_num))
        else:
            self.label_1.setText('The number needs to be greater than 1')
            self.input_text.clear()


class CollatzCalculator(object):

    def isValid(self, input_num):
        if not input_num.isdigit():
            return False
        num = int(input_num)
        if num <= 1:
            return False
        return True

    def odd(self, num):
        return num*3 + 1

    def even(self, num):
        return num/2

    def num_recursions(self, num):
        num_times = 0
        temp_num = num
        while temp_num != 1:
            if temp_num % 2 == 0:
                temp_num = self.even(temp_num)
            else:
                temp_num = self.odd(temp_num)
            num_times += 1

        return num_times


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())

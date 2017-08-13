# -------------------------------
# Author        # Ethan Shapiro
# Project Name  # Distance Between Cities
# Last Updated  # 7/23/2017
# --------------------------------
# Let a user input two locations and a unit distance they want specified

import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QLineEdit, QApplication, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtCore import Qt


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()
        self.setLayout(self.main_layout)

        self.show()

    def init_ui(self):
        loc_1_line_edit = QLineEdit()
        loc_label_1 = QLabel('Location 1')
        loc_2_line_edit = QLineEdit()
        loc_label_2 = QLabel('Location 2')
        dist_label = QLabel('0')
        enter_button = QPushButton('Enter')
        dropdown_box = QComboBox()
        dropdown_box.addItem('mi')
        dropdown_box.addItem('km')

        self.main_layout = QVBoxLayout(self)

        child_h_layout = QHBoxLayout()
        child_h_layout.addStretch()
        child_h_layout.addWidget(enter_button)
        child_h_layout.addWidget(dropdown_box)
        child_h_layout.addStretch()

        self.main_layout.addWidget(loc_label_1)
        self.main_layout.addWidget(loc_1_line_edit)
        self.main_layout.addWidget(loc_label_2)
        self.main_layout.addWidget(loc_2_line_edit)
        self.main_layout.addWidget(dist_label)
        self.main_layout.addLayout(child_h_layout)

class DistanceCalculator(object):

    earth_distances = {
    'mi': 3959,
    'km': 6371
    }

    def calculate_distance(self, loc_1, loc_2, unit):
        pass

app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())

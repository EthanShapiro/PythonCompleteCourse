# ----------------------------------
#   Ethan Shapiro
#   Quiz Maker
#   Date Created 7/15/2017
#   Date Last Edited
# ----------------------------------
#
#   Quiz Maker gets 5 questions from a file and shows them to the user
#   User answers, and they are compared to an answer key file

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QRadioButton, QApplication, QButtonGroup
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt
import json


class DataGetter(object):

    @staticmethod
    def get_data(data_type=None):
        # User can enter question type if they want
        if data_type:
            pass
        else:
            with open('questions.json', 'r') as f:
                return json.load(f)


class QuizMaker(object):

    def __init__(self):
        self.questions = DataGetter.get_data()

    def init_correct_answers(self):
        pass

    def compare_answers(self, answers):
        correct = 0
        for q_a in answers:
            if self.questions[q_a[0]]['ca'] == q_a[1]:
                correct += 1
        return correct

class Gui(QWidget):
    def __init__(self):
        super().__init__()

        self.quiz_maker = QuizMaker()
        self.show()
        self.setGeometry(250, 250, 200, 200)
        self.answer_groups = []
        self.question_answer = []
        self.init_gui()

    def init_gui(self):
        self.main_layout = QVBoxLayout(self)

        for q in self.quiz_maker.questions.values():
            self.answer_groups.append(self.init_question(q))

        self.question_answer = [[q] for q in self.quiz_maker.questions.keys()]


        bottom_layout = QHBoxLayout()
        enter_button = QPushButton('Enter')
        enter_button.released.connect(self.confirm_answers)

        self.correct_label = QLabel()
        bottom_layout.addWidget(enter_button)
        bottom_layout.addWidget(self.correct_label)

        self.main_layout.addLayout(bottom_layout)

        self.setLayout(self.main_layout)

    def confirm_answers(self):
        for i, a in enumerate(self.answer_groups):
            self.question_answer[i].append(a.checkedButton().text()[0])
        num_correct = self.quiz_maker.compare_answers(self.question_answer)
        self.correct_label.setText(str(num_correct))


    def init_question(self, question):
        a_d = 'abcd'
        q_layout = QVBoxLayout(self)
        q_label = QLabel(question['q'])
        q_label.setAlignment(Qt.AlignBottom)
        q_layout.addWidget(q_label)
        button_group = QButtonGroup()
        for i, a in enumerate(question['a'].split(',')):
            answer = QRadioButton('{0}: {1}'.format(a_d[i], a))
            answer.toggle()
            button_group.addButton(answer)
            q_layout.addWidget(answer)
        self.main_layout.addLayout(q_layout)
        return button_group

app = QApplication(sys.argv)
quiz_maker = Gui()
sys.exit(app.exec())

import random
import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QPushButton, QGridLayout, QMessageBox

from styleState import StyleState
from utils import Utils
#from src.buttonFactory import playground


class GameFactory:

    def __init__(self, button_number: int, mine_number: int, row_number: int, col_number: int, main_window):
        self.button_number = button_number
        self.mine_number = mine_number
        self.row_number = row_number
        self.col_number = col_number
        self.main_window = main_window

        self.playground = Utils.make_playground(button_number, mine_number)
        self.flag_number = 0
        self.arr = [[0] * (col_number + 2) for _ in range(row_number + 2)]
        self.buttons = [[QPushButton() for _ in range(col_number)] for _ in range(row_number)]

        Utils.make_info(row_number, col_number, self.playground, self.arr)


    def __call__(self, layout: QGridLayout):
        for i in range(1, self.row_number+1):
            for j in range(1, self.col_number+1):
                button: QPushButton = self.buttons[i-1][j-1]
                button.is_flag = False

                if self.arr[i][j] == -1:
                    button.clicked.connect(self.hit_mine)
                elif self.arr[i][j] == 0:
                    button.clicked.connect(lambda ch,
                                                  row=i,
                                                  col=j,
                                                  row_number=self.row_number,
                                                  col_number=self.col_number,
                                                  buttons=self.buttons,
                                                  arr=self.arr,:
                                           Utils.open_empty_cell(row-1, col-1, row_number, col_number, buttons, arr))
                else:
                    button.clicked.connect(lambda ch, btn=button, row=i, col=j: self.hit_not_mine(btn, row, col))

                button.mousePressEvent = lambda event, btn=button: self.handle_right_click(event, btn)
                button.setFixedSize(100, 100)
                layout.addWidget(button, i-1, j-1)


    def hit_mine(self) -> None:
        for i in range(self.row_number):
            for j in range(self.col_number):
                StyleState.set_defaults_style(self.buttons[i][j], self.arr[i+1][j+1])
                self.buttons[i][j].setEnabled(False)

        reply = QMessageBox.critical(None, "Game Over", "You hit a mine! do you want play again?", QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.main_window.restart_game()
        else:
            sys.exit()


    def hit_not_mine(self, button, row, col):
        number = self.arr[row][col]

        StyleState.set_defaults_style(button, number)



    def handle_right_click(self, event, button: QPushButton):
        if event.button() == Qt.RightButton:
            if button.is_flag:
                button.setIcon(QIcon())
                button.is_flag = False
                self.flag_number -= 1
            else:
                button.setIcon(QIcon("../assets/images/flag.png"))
                button.setIconSize(QSize(64, 64))
                button.is_flag = True
                self.flag_number += 1
            self.update_flag_label()
            if self.flag_number == self.mine_number:
                self.check_win()

        if event.button() == Qt.LeftButton and not button.is_flag:
            button.click()

    def update_flag_label(self):
        self.main_window.flag_counter_label.setText(f" Flags: {self.flag_number}/{self.mine_number}")

    def check_win(self):
        correct_number = 0

        for i in range(self.row_number):
            for j in range(self.col_number):
                button = self.buttons[i][j]
                if button.is_flag and self.arr[i+1][j+1] == -1:
                    correct_number += 1

        if correct_number == self.mine_number:
            reply = QMessageBox.information(None, "YOU WIN!",
                                            "LOL, \n do you want play again?",
                                            QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.main_window.restart_game()
            else:
                sys.exit()

import logging

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QGridLayout, QMessageBox

from style.styleState import StyleState
from utils.utils import Utils
#from src.buttonFactory import playground

logging.basicConfig(level=logging.INFO, format="%(name)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)



class GameFactory:

    def __init__(self, button_number: int, row_number: int, col_number: int, setup_window):
        self.button_number = button_number
        self.mine_number = Utils.calc_number_mine(button_number)
        self.row_number = row_number
        self.col_number = col_number
        self.setup_window = setup_window

        self.playground = Utils.make_playground(button_number, self.mine_number)
        self.flag_number = 0
        self.arr = [[0] * (col_number + 2) for _ in range(row_number + 2)]
        self.buttons = [[QPushButton() for _ in range(col_number)] for _ in range(row_number)]

        logger.info(f"CREATING THE GAME")

        Utils.make_info(row_number, col_number, self.playground, self.arr)


    def __call__(self, layout: QGridLayout):
        self.flag_number = 0
        button_size = Utils.calc_button_size(self.button_number)
        logger.info(f"GAME IS STARTING: CELL NUMBER: {self.button_number}, MINE NUMBER: {self.mine_number}")
        for i in range(1, self.row_number+1):
            for j in range(1, self.col_number+1):
                button: QPushButton = self.buttons[i-1][j-1]
                button.is_flag = False
                button.is_clicked = False

                if self.arr[i][j] == -1:
                    button.clicked.connect(self.hit_mine)
                elif self.arr[i][j] == 0:
                    button.clicked.connect(lambda ch, row=i,col=j,
                                                  row_number=self.row_number,
                                                  col_number=self.col_number,
                                                  buttons=self.buttons, arr=self.arr,:
                                           Utils.open_empty_cell(row-1, col-1, row_number, col_number, buttons, arr))
                else:
                    button.clicked.connect(lambda ch, btn=button, row=i, col=j: self.hit_not_mine(btn, row, col))

                button.mousePressEvent = lambda event, btn=button: self.handle_right_click(event, btn)
                button.setFixedSize(button_size, button_size)
                layout.addWidget(button, i-1, j-1)
        self.update_flag_label()



    def hit_mine(self) -> None:
        for i in range(self.row_number):
            for j in range(self.col_number):
                StyleState.set_defaults_style(self.buttons[i][j], self.arr[i+1][j+1], isEnd=True)

        logger.info("HIT MINE, USER LOSE")
        reply = QMessageBox.critical(None, "Game Over", "You hit a mine! do you want play again?", QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.setup_window.restart_game(self.button_number, self.row_number, self.col_number)


    def hit_not_mine(self, button, row, col):
        number = self.arr[row][col]
        button.is_clicked = True

        StyleState.set_defaults_style(button, number)

        if (self.flag_number == self.mine_number and
                self.button_number - self.mine_number == Utils.count_pressed_buttons(self.buttons)):

            self.check_win()


    def handle_right_click(self, event, button: QPushButton):
        if event.button() == Qt.RightButton:
            StyleState.set_flag_style(button)
            self.flag_number += [1, -1][button.is_flag]
            button.is_flag = not button.is_flag
            self.update_flag_label()


        if event.button() == Qt.LeftButton and not button.is_flag:
            button.click()


    def update_flag_label(self):
        self.setup_window.main_window.status_bar.showMessage(f"flags: {self.flag_number}/{self.mine_number}")


    def check_win(self):
        correct_number = 0

        for i in range(self.row_number):
            for j in range(self.col_number):
                button = self.buttons[i][j]
                if button.is_flag and self.arr[i+1][j+1] == -1:
                    correct_number += 1

        if correct_number == self.mine_number:
            reply = QMessageBox.information(None, "YOU WIN!",
                                            "LOL \n do you want play again?",
                                            QMessageBox.Yes | QMessageBox.No)
            logger.info("USER WIN")
            if reply == QMessageBox.Yes:
                self.setup_window.restart_game(self.button_number, self.row_number,
                                                  self.col_number)



import random
import math

from PyQt5.QtWidgets import QPushButton

from style.styleState import StyleState

class Utils:
    compnents = ((-1, -1),
                 (0, -1),
                 (1, -1),
                 (-1, 0),
                 (1, 0),
                 (-1, 1),
                 (0, 1),
                 (1, 1)
                 )
    @staticmethod
    def make_playground( button_number: int, mine_number: int) -> list[int]:
        buttons = [0] * (button_number - mine_number) + [1] * mine_number
        random.shuffle(buttons)
        #return [1, 1, 1, 1,  0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0]
        return buttons


    @staticmethod
    def make_info(row_number, col_number, playground, arr):
        temp = 0

        for i in range(1, row_number+1):
            for j in range(1, col_number+1):
                if playground[temp] == 1:
                    arr[i][j] = -1

                    for x, y in Utils.compnents:
                        if arr[i+x][j+y] != -1:
                            arr[i+x][j+y] += 1
                temp += 1


    @staticmethod
    def open_empty_cell(row: int, col: int, row_number: int, col_number: int, buttons: list[list[QPushButton]], arr: list[list[int]]):
        def dfs(i, j):
            if i < 0 or i >= row_number or j < 0 or j >= col_number or arr[i + 1][j + 1] == -2:
                return

            button = buttons[i][j]
            number = arr[i + 1][j + 1]
            button.is_clicked = True
            if button.is_flag:
                return

            if number != 0:
                StyleState.set_defaults_style(button, number)
                return

            new_number = arr[i + 1][j + 1] = -2

            for x, y in Utils.compnents:
                dfs(i + x, j + y)

            StyleState.set_defaults_style(button, new_number)
        dfs(row, col)


    @staticmethod
    def count_pressed_buttons(buttons: list[list[QPushButton]]) -> int:
        count = 0
        for row_buttons in buttons:
            count += sum(button.is_clicked for button in row_buttons)

        return count


    @staticmethod
    def calc_number_mine(buttons_number: int):
        return {
        64: 16,
        144: 30,
        256: 56
    }.get(buttons_number, 20)



    @staticmethod
    def calc_button_size(buttons_number: int) -> int:
         return {
        64: 90,
        144: 65,
        256: 40
    }.get(buttons_number, 20)


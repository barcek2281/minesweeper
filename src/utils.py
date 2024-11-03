
import random

from PyQt5.QtWidgets import QPushButton

from styleState import StyleState

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
        buttons = [0] * (button_number - mine_number) + [1] * (mine_number)
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
        def dfs(row, col):
            if row < 0 or row >= row_number or col < 0 or col >= col_number or arr[row+1][col+1] == -2:
                return
            button = buttons[row][col]
            number = arr[row + 1][col + 1]

            if number != 0:
                StyleState.set_defaults_style(button, number)
                return

            new_number = arr[row+1][col+1] = -2

            for x, y in Utils.compnents:
                dfs(row+x, col+y)

            StyleState.set_defaults_style(button, new_number)
        dfs(row, col)
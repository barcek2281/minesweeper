
"""
 -2 - пустая клетка которая была нажата
 -1 - Мина
  0 - пустая клетка которая НЕ была нажата
 последущие цифры, обазначают число мин рядом
"""
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon


class StyleState:
    color = {
        -2: "grey",
        -1: "red",
        0: "grey",
        1: "blue",
        2: "green",
        3: "red",
        4: "purple",
        5: "maroon",
        6: "turquoise",
        7: "black",
        8: "gray"
    }

    @staticmethod
    def set_defaults_style(button: QPushButton, number: int):
        if number < -2 or number > 8:
            raise ValueError(f"Number must be between -2 and 8 ([-2;8])")
        {
            -2: StyleState._empty_cell,
            0: StyleState._empty_cell,
            -1: StyleState._mine_cell,
        }.get(number, StyleState._open_cell)(button, number)

        button.setEnabled(False)

    @staticmethod
    def _empty_cell(button: QPushButton, number: int):
        flag = button.is_flag

        if flag:
            button.setIcon(QIcon("../assets/images/mine.png"))
            return

        button.setStyleSheet(
            f"color: {StyleState.color[number]}; font-weight: bold; font-size: 24px; background-color: gray")

    @staticmethod
    def _mine_cell( button: QPushButton, number: int):
        button.setIcon(QIcon("../assets/images/mine.png"))
        button.setIconSize(QSize(64, 64))

    @staticmethod
    def _open_cell( button: QPushButton, number: int):
        button.setText(str(number))
        button.setStyleSheet(f"color: {StyleState.color[number]}; font-weight: bold; font-size: 30px;")
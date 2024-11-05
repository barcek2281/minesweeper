
"""
 -2 - пустая клетка которая была нажата
 -1 - Мина
  0 - пустая клетка которая НЕ была нажата
 последущие цифры, обазначают число мин рядом
"""
import os
import sys

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon

def resource_path(relative_path):
    """ Возвращает путь к ресурсу, который работает как для исходного кода, так и для скомпилированного приложения """
    try:
        # Если приложение запущено в собранной версии
        base_path = sys._MEIPASS
    except Exception:
        # Если приложение запущено из исходников
        base_path = os.path.abspath("..")
    return os.path.join(base_path, relative_path)

CURRENT_DIR = os.path.dirname(__file__)
FLAG_PATH = resource_path("assets/images/flag.png")
MINE_PATH = resource_path("assets/images/mine.png")
CROSS_PATH = resource_path("assets/images/red_cross.png")

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
    def set_defaults_style(button: QPushButton, number: int, isEnd: bool=False):
        if number < -2 or number > 8:
            raise ValueError(f"Number must be between -2 and 8 ([-2;8])")
        {
            -2: StyleState._empty_cell,
            0: StyleState._empty_cell,
            -1: StyleState._mine_cell,
        }.get(number, StyleState._open_cell)(button, number, isEnd)

        button.setEnabled(False)

    @staticmethod
    def _empty_cell(button: QPushButton, number: int, isEnd: bool=False):
        if button.is_flag and isEnd:
            button.setIcon(QIcon(CROSS_PATH))
            button.setIconSize(QSize(56, 56))
            return

        button.setStyleSheet(
            f"color: {StyleState.color[number]}; "
            f"font-weight: bold; font-size: 24px;"
            f" background-color: gray")


    @staticmethod
    def _mine_cell( button: QPushButton, number: int, isEnd: bool=False):
        if button.is_flag:
            button.setIcon(QIcon(FLAG_PATH))
        else:
            button.setIcon(QIcon(MINE_PATH))
        button.setIconSize(QSize(56, 56))


    @staticmethod
    def _open_cell( button: QPushButton, number: int, isEnd: bool=False):
        if button.is_flag:
            button.setIcon(QIcon(CROSS_PATH))
            button.setIconSize(QSize(56, 56))
            return

        button.setText(str(number))
        button.setStyleSheet(f"color: {StyleState.color[number]}; font-weight: bold; font-size: 30px;")


    @staticmethod
    def set_flag_style(button: QPushButton):

        if button.is_flag:
            button.setIcon(QIcon())
        else:
            button.setIcon(QIcon(FLAG_PATH))
        button.setIconSize(QSize(56, 56))


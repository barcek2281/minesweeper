import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtCore import Qt

from src.gameFactory import GameFactory

HEIGHT = 600
WIDTH = 600
BUTTON_NUMBER = 64
MINE_NUMBER = 10
ROW_NUMBER = 8
COL_NUMBER = 8

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUI__()


    def __initUI__(self):
        self.setWindowTitle('Minesweeper')
        self.setGeometry(700, 300, WIDTH, HEIGHT)

        # Централизация виджетов
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        self.box_layout = QVBoxLayout(central_widget)
        self.grid_layout = QGridLayout()

        self.init_game()

    def init_game(self):
        top_layout = QHBoxLayout()

        self.flag_counter_label = QLabel(f"Flags: 0/{MINE_NUMBER}")
        #self.flag_counter_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.flag_counter_label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        top_layout.addWidget(self.flag_counter_label)
        # top_layout.addStretch()

        self.box_layout.addLayout(top_layout)
        self.box_layout.addLayout(self.grid_layout)
        self.playgroundFactory = GameFactory(BUTTON_NUMBER,
                                             MINE_NUMBER,
                                             ROW_NUMBER,
                                             COL_NUMBER,
                                             main_window=self)
        self.playgroundFactory(self.grid_layout)

    def restart_game(self):
        for i in reversed(range(self.grid_layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()
        self.init_game()
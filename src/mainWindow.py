from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QStatusBar, QAction

from Engine.gameSetup import GameSetup

HEIGHT = 600
WIDTH = 600

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUI__()


    def __initUI__(self):
        self.setWindowTitle('Minesweeper')
        self.setGeometry(720, 270, WIDTH, HEIGHT)

        # Централизация виджетов
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.grid_layout = QGridLayout(self.central_widget)

        self.setup_game = GameSetup(self, self.grid_layout)
        self.setup_game()

        # Статус-бар
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        # Меню
        menu_bar = self.menuBar()

        # Меню "Minesweeper"
        game_menu = menu_bar.addMenu("Game")
        # Пункт меню "Change Difficulty"
        change_difficulty_action = QAction("Change Difficulty", self)
        change_difficulty_action.setShortcut("Ctrl+E")
        change_difficulty_action.triggered.connect(self.setup_game)
        game_menu.addAction(change_difficulty_action)

        # Пункт меню "Exit"
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        game_menu.addAction(exit_action)

        # # Централизация виджетов
        # self.central_widget = QWidget(self)
        # self.setCentralWidget(self.central_widget)
        # self.grid_layout = QGridLayout(self.central_widget)


    # def setup_game(self):
    #     self.clear_layout()
    #
    #     for size in [8, 12, 16]:
    #         button = QPushButton(f"{size} x {size}")
    #         button.setFixedSize(200, 200)
    #         button.clicked.connect(lambda _, button_number=size,  row_number=size, col_number=size: self.restart_game(button_number*button_number, row_number, col_number))
    #         self.grid_layout.addWidget(button)
    #
    #
    #
    # def init_game(self, button_number, row_number, col_number):
    #     self.playgroundFactory = GameFactory(button_number,
    #                                          row_number,
    #                                          col_number,
    #                                          main_window=self)
    #     self.playgroundFactory(self.grid_layout)
    #
    #
    # def restart_game(self, button_number, row_number, col_number):
    #     self.clear_layout()
    #     self.init_game(button_number, row_number, col_number,)
    #
    #
    # def clear_layout(self, layout=None):
    #     if layout is None:
    #         layout = self.grid_layout
    #     while layout.count():
    #         item = layout.takeAt(0)
    #         widget = item.widget()
    #         if widget is not None:
    #             widget.deleteLater()  # Полностью удаляет виджет
    #         elif item.layout() is not None:
    #             self.clear_layout(item.layout())  # Рекурсивно очищает вложенные лейауты
    #
    #         # Шаг 2: Удаляем сам self.box_layout из self.central_widget

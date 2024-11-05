
from PyQt5.QtWidgets import QPushButton

from src.Engine.gameFactory import GameFactory

class GameSetup:
    def __init__(self, main_window, layout):
        self.main_window = main_window
        self.layout = layout
        self.gameFactory = None

    def __call__(self):
        self.clear_layout()

        for size in [8, 12, 16]:
            button = QPushButton(f"{size} x {size}")
            button.setFixedSize(200, 200)
            button.clicked.connect(lambda _, button_number=size,  row_number=size, col_number=size: self.restart_game(button_number*button_number, row_number, col_number))
            self.layout.addWidget(button)



    def init_game(self, button_number, row_number, col_number):
        self.gameFactory = GameFactory(button_number,
                                             row_number,
                                             col_number,
                                              setup_window=self)
        self.gameFactory(self.layout)


    def restart_game(self, button_number, row_number, col_number):
        self.clear_layout()
        self.init_game(button_number, row_number, col_number)


    def clear_layout(self, layout=None):
        if layout is None:
            layout = self.layout

        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()  # Полностью удаляет виджет
            elif item.layout() is not None:
                self.clear_layout(item.layout())  # Рекурсивно очищает вложенные лейауты

            # Шаг 2: Удаляем сам self.box_layout из self.central_widget
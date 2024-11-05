import sys
import logging

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import mainWindow


#TODO: Сделать новые пнг файлы для неправильно выставленных флагов DONE
#TODO: статус бар сверху, чтобы сочетание клавиш работало DONE


if __name__ == '__main__':
    app = QApplication([])
    app.setStyle('Windows')
    window = mainWindow.MainWindow()
    window.show()
    app.exec_()


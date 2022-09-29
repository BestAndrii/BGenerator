"""Основной модуль. Создаёт программу и обработчики интерфейса."""


import sys

from random import randint

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from des import Ui_MainWindow


class Window(QMainWindow):
    """Создаёт окно программы."""

    def __init__(self):
        super().__init__()

        # Загрузка дизайна в окно
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Обработчик кнопки
        self.ui.pushButton.clicked.connect(self.generate_number)

    def generate_number(self):
        """Генерирует случайное число."""
        with_ = self.ui.lineEdit.text()
        to = self.ui.lineEdit_2.text()

        try:
            if with_:
                if to:
                    number = QMessageBox()
                    number.setText(f"Случайное число: {randint(int(with_), int(to)) }")
                    number.exec_()

                else:
                    warning = QMessageBox()
                    warning.setText("Вы не ввели до какого числа генерировать число")
                    warning.exec_()

            else:
                warning = QMessageBox()
                warning.setText("Вы не ввели с какого числа генерировать число")
                warning.exec_()

        except ValueError:
            warning = QMessageBox()
            warning.setText("Проверьте правильность ввода данных")
            warning.exec_()


def start_app():
    """Запускает приложение."""
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    start_app()

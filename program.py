########################################################################################################################
##
## BY: AFONIN VLADIMIR ALEKSEEVICH
##
## PROJECT: GYROTRON CAVITY GUI
##
## V: 1.0.0
##
########################################################################################################################

r'''
.. include:: README.md
'''

from Gyrotron_Cavity_GUI import *
import sys


class Program:
    """
    В данном классе реализуется метод отображающий графического интерфейса программы
    """
    def __init__(self):
        """
        .. include:: Documentation/MarkdownFiles/program.md
        """
        if __name__ == "__main__":
            app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
            MainWindow = QtWidgets.QMainWindow()  # Создаём объект класса QMainWindow
            ui = Ui_MainWindow()  # Создаём объект класса Ui_MainWindow из файла Gyrotron_Cavity_GUI.py
            ui.setupUi(MainWindow)  # Вызываем метод setupUi из класса Ui_MainWindow с параметром MainWindow
            MainWindow.show()  # Отображает окно
            app.exec_()  # Запуск приложения


Program()

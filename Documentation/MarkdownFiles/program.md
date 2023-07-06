`__init__()` - это специальный метод, который вызывается при создании объекта. 
В этом методе происходит инициализация всех атрибутов класса. По сути, это конструктор класса. 

Источники:
- [Документация Python](https://docs.python.org/3/tutorial/classes.html) (en)
- [Лаборатория линуксоида](https://younglinux.info/oopython/init) (ru)

`if __name__ == "__main__":` - данная конструкция проверяет, был ли файл запущен напрямую.
Переменная `__name__` - это специальная переменная, которая будет равна `"__main__"`, 
только если файл запускается как основная программа, и выставляется равной имени модуля при импорте модуля.
Если же ссылаться на файл как на модуль, то содержимое конструкции `if` не будет выполнено.

Источники:
- [Документация Python](https://docs.python.org/3/library/__main__.html) (en)
- [PythonRU](https://pythonru.com/uroki/funkcija-main-v-python-dlja-nachinajushhih) (ru)
- [Python для сетевых инженеров](https://pyneng.readthedocs.io/ru/latest/book/11_modules/if_name_main.html) (ru)

Функция `sys.argv` модуля `sys` возвращает список параметров командной строки, передаваемых скрипту Python.

Источники:
- [Документация Python](https://docs.python.org/3/library/sys.html) (en)
- [Функция argv модуля sys в Python](https://docs-python.ru/standart-library/modul-sys-python/funktsija-argv-modulja-sys/) (ru)

Метод `exec_()` запускает цикл обработки событий, без этого цикла не будут работать виджеты.
QApplication используется для доставки сообщений/событий объектам Qt, а также для взаимодействия
с "окружающей средой", например оконным менеджером операционной системы.  
Источник: [stackoverflow](https://ru.stackoverflow.com/questions/748124/Разъясните-своими-словами-что-такое-app-exec-и-что-оно-делает-в-pyqt5)


Графический интерфейс реализован с помощью библиотеки [PyQt5](https://doc.qt.io/).
Более подробно с библиотекой можно ознакомиться здесь:
- [Документация PyQt5](https://doc.qt.io/) (en)
- [PyQt5 наPyPI](https://pypi.org/project/PyQt5/#description) (en)
- [Руководство по PyQt5](https://python-scripts.com/pyqt5) (ru)
- [PyQt5: первые программы](https://pythonworld.ru/gui/pyqt5-firstprograms.html) (ru)
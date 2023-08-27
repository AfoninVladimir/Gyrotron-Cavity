########################################################################################################################
##
## BY: AFONIN VLADIMIR ALEKSEEVICH
##
## PROJECT: GYROTRON CAVITY GUI
##
## V: 1.0.0
##
########################################################################################################################
"""
## Модуль построения графиков распределения *модуля* комплексных амплитуд полей мод вдоль резонатора и распределения
*фазы* комплексных амплитуд полей мод вдоль резонатора.

В данном файле находится один основной метод, строящая графики, и 5 вспомогательных,
считывающие и обрабатывающие данный из файла *MathExport1.dat*
"""
from imports import *


def plot_mods(k, zi):
    '''
    Данный метод строит график распределения k-й мод и фаз в раздельных окнах.

    Метод использует 3 вспомогательных метода:
    - complex_abs()
    - complex_arg()
    - read_file()

    Принимает на вход:

    k:
    - порядковый номер моды
    - тип: целое число (int)

    zi:
    - значения узлов сетки
    -тип: numpy.ndarray (массив)
    - длина: NN

    Переменные:

    n: индекс числа ближайшего к нулю для нормировки
    ([argsort](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html))
    '''

    def read_file(k):
        r"""
        Данный метод используется в `charting_module` для считывания данных из файла созданного вычислительным модулем.
        Он использует 2 вспомогательных модуля: `read_num_comp` и `read_num`.
        """

        file = open("MathExport1.dat", "r", encoding="utf-8")

        for i in range(3):
            file.readline()

        R = []
        eigenvalues = []
        """Dimensionless frequencies OmegaL2divR2:"""
        dim_freq = read_num_comp(file)
        eigenvalues.append(dim_freq)

        # Calculated number of eigenvalues
        mods = int(file.readline().split("=")[1])

        for i in range(3):
            file.readline()

        """Calculated Eigenvalues:"""
        calcul_eigenval = read_num_comp(file)
        eigenvalues.append(calcul_eigenval)

        # Number of grid points
        NN = int(file.readline().split("=")[1])

        for i in range(3):
            file.readline()
        # Z - coordinate of grid points:
        z = read_num(file)
        file.readline()

        # Eigenvector`s
        for i in range(mods):
            file.readline()
            file.readline()
            R.append(read_num_comp(file))
            file.readline()

        file.close()

        # Возвращает решения в узлах для k-й моды
        return R[k]

    def read_num_comp(file):
        """
        Метод считывает комплексные числа из файла созданного вычислительным модулем на Fortran.
        """
        nums = []
        reim = []

        # пока в строке есть символ ":", будет происходить считывание чисел и запись их в массив reim
        while ":" in (st := file.readline()):
            nums.append(st[st.index(":") + 2: -3])
        nums = "  ".join(nums).split(")  (")
        for i in range(len(nums)):
            nums[i] = nums[i].replace("(", "").replace(")", "").replace("D", "e")
            b = nums[i].split(",")
            reim.append(complex(float(b[0]), float(b[1])))
        return reim

    def read_num(file):
        """
        Метод считывает числа Z - coordinate of grid points из файла созданного вычислительным модулем на Fortran.
        """
        nums_z = []
        nums = []
        while ":" in (st := file.readline()):
            nums.append(st[st.index(":") + 4: -1])
        nums = "  ".join(nums).split(")  (")
        for i in range(len(nums)):
            nums[i] = nums[i].replace("(", "").replace(")", "").replace("D", "e")
            nums_z = nums[i].split("  ")

        for j in range(len(nums_z)):
            nums_z[j] = float(nums_z[j])
        return nums_z

    def complex_abs(comp):
        """
        Метод находит модуль комплексного числа.

        Принимает на вход:

        comp:
        - тип: список (list)
        - тип параметров: комплексное число (complex)
        - длина: произвольная

        Возвращает:
        comp:
        - тип: список (list)
        - тип параметров: число с плавающей точкой (float)
        - длина: без изменений
        """

        for i in range(len(comp)):
            comp[i] = np.abs(comp[i])
        return comp

    def complex_arg(comp, n):
        """
        Метод находит аргумент комплексного числа

        Принимает на вход:

        comp:
        - тип: список (list)
        - тип параметров: комплексное число (complex)
        - длина: произвольная

        Возвращает:
        Compl:
        - тип: список (list)
        - тип параметров: число с плавающей точкой (float)
        - длина: длина comp

        [cmath.phase()](https://docs.python.org/3/library/cmath.html)
        """

        Compl = []
        for i in range(len(comp)):
            Compl.append(cmath.phase(comp[i] / comp[n]))
        return Compl

    n = np.argsort(np.abs(zi))[0]
    """Построение графиков мод"""
    plt.figure(f"Мода %2d" % (k + 1))  # Название окна графика
    plt.grid()  # Отображает сетку
    plt.xlabel("z, м")  # Подпись к оси x
    plt.ylabel("F, a.e.")  # Подпись к оси y
    plt.plot(zi, complex_abs(read_file(k)))  # Построение графиков (plot(x, y),
    # где x и y - массивы(списки) одинаковой длины)

    """Построение графиков фаз"""
    plt.figure(f"Фаза %2d" % (k + 1))  # Название окна графика
    plt.grid()  # Отображает сетку
    plt.xlabel("z, м")  # Подпись к оси x
    plt.ylabel("Arg F, рад")  # Подпись к оси y
    plt.plot(zi, complex_arg(read_file(k), n))  # Построение графиков (plot(x, y) ,
    # где x и y - массивы(списки) одинаковой длины)

    plt.show()  # Отображает окна (https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html)

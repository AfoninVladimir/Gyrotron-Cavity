########################################################################################################################
##
## BY: AFONIN VLADIMIR ALEKSEEVICH
##
## PROJECT: GYROTRON CAVITY GUI
##
## V: 0.6.0
##
########################################################################################################################
import matplotlib.pyplot as plt
import numpy as np

v = []


def plot_mods(k, zi):
    # чтение из фалай (вычислительного модуля)
    def read_file(l):
        # считатет кол-во строк
        def inter(x):
            nn = x // 3
            if x % 3 != 0:
                nn += 1
            return nn

        # считывает данные
        def function(k):
            func2 = ""
            mod2 = []
            mod = []
            for i in range(k):
                func2 += file.readline()
            func2 = func2.splitlines()
            for i in func2:
                mod.append(i.split("  "))
            for i in range(len(mod)):
                mod2 += mod[i]
            return mod2

        # считывание комплексного числа
        def fan(x):
            a = []
            c = []
            for i in x:
                a.append(i[i.index('(') + 1:i.index(')')])
            for i in a:
                b = i.split(", ")
                c.append(complex(float(b[0]), float(b[1])))
            return c

        file = open("MathExport.dat", "r")
        func1 = file.readline().split()
        NN = int(func1[0])
        mods = int(func1[1])

        nn = inter(NN)
        mod = inter(mods)
        f = file.readline()

        furt = []
        rts = []

        # собственные числа
        global v
        v = fan(function(mod))
        f = file.readline()

        for i in range(mods // 2):
            rts1 = file.readline().split()
            rts.append(float(rts1[0]))
            rts.append(float(rts1[1]))

        # считывание координат точек
        for i in range(mods):
            f = file.readline()
            furt.append(function(nn))

        for i in range(len(furt)):
            furt[i] = fan(furt[i])
        file.close()

        return furt[l]

    # модуль комплексного числа
    def complex_abs(comp):
        for i in range(len(comp)):
            comp[i] = np.abs(comp[i])
        return comp

    # # аргумент комплексного числа
    def complex_arg(x):
        Re = []
        Im = []
        Compl = []
        for i in x:
            Re.append(i.real)
            Im.append(i.imag)

        for i in range(len(Re)):
            Compl.append(-np.arctan2(Re[i], Im[i]))

        return Compl

    # построение графиков
    plt.figure(2 * (k + 1))
    plt.xlabel("z, мм")
    plt.ylabel("R(z),мм")
    plt.grid()
    plt.plot(zi, complex_abs(read_file(k)))

    plt.figure((2 * (k + 1)) + 1)
    plt.xlabel("z, мм")
    plt.ylabel("R(z),мм")
    plt.grid()
    plt.plot(zi, complex_arg(read_file(k)))

    plt.show()

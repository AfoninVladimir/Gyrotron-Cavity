########################################################################################################################
##
## BY: AFONIN VLADIMIR ALEKSEEVICH
##
## PROJECT: GYROTRON CAVITY GUI
##
## V: 1.0.0
##
########################################################################################################################
import matplotlib.pyplot as plt

from import_all import *


def plot_mods(k, zi):
    # чтение из фалай (вычислительного модуля)
    def read_file(l):

        def read_num_comp(file):
            nums = []
            reim = []
            while ":" in (st := file.readline()):
                nums.append(st[st.index(":") + 2: -3])
            nums = "  ".join(nums).split(")  (")
            for i in range(len(nums)):
                nums[i] = nums[i].replace("(", "").replace(")", "").replace("D", "e")
                b = nums[i].split(",")
                reim.append(complex(float(b[0]), float(b[1])))
            return reim

        def read_num(file):
            nums_z = []
            nums = []
            reim = []
            while ":" in (st := file.readline()):
                nums.append(st[st.index(":") + 4: -1])
            nums = "  ".join(nums).split(")  (")
            for i in range(len(nums)):
                nums[i] = nums[i].replace("(", "").replace(")", "").replace("D", "e")
                nums_z = nums[i].split("  ")

            for j in range(len(nums_z)):
                nums_z[j] = float(nums_z[j])
            return nums_z

        file = open("MathExport1.dat")

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

        return R[l]

    # модуль комплексного числа
    def complex_abs(comp):
        for i in range(len(comp)):
            comp[i] = np.abs(comp[i])
        return comp

    # аргумент комплексного числа
    def complex_arg(x):
        Compl = []

        for i in range(len(x)):
            Compl.append(-np.arctan2(x[i].real, x[i].imag))

        n = Compl.index(min(Compl, key=abs))

        for i in range(len(Compl)):
            Compl[i] = Compl[i] / -np.arctan2(x[n].real, x[n].imag)
        return Compl


    # построение графиков
    plt.figure(f"Мода %2d" % (k+1))
    plt.xlabel("z, мм")
    plt.ylabel("R(z),мм")
    plt.grid()
    plt.plot(zi * 1000, complex_abs(read_file(k)))

    plt.figure(f"Фаза %2d" % (k+1))
    plt.xlabel("z, мм")
    plt.ylabel("R(z),мм")
    plt.grid()
    plt.plot(zi * 1000, complex_arg(read_file(k)))

    plt.show()

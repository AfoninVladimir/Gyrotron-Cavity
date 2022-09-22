########################################################################################################################
##
## BY: AFONIN VLADIMIR ALEKSEEVICH
##
## PROJECT: GYROTRON CAVITY GUI
##
## V: 0.6.0
##
########################################################################################################################
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5 import *
import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy import special
from numpy import array  # массив
from numpy import arange  # как range, но с шагом типа float
from numpy import pi
from numpy import sin, cos, tan, arcsin, arccos, arctan, sinh, cosh, tanh, arcsinh, arccosh, arctanh
from numpy import degrees  # Преобразует радианную меру угла в градусную.
from numpy import radians  # Преобразует градусную меру угла в радианную.
from plot_mods import plot_mods
from auxiliary_functions import *

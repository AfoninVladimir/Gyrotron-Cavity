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
.. include:: Documentation/MarkdownFiles/imports.md
'''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5 import *
import os
import sys
import time
import cmath
import subprocess
import matplotlib.pyplot as plt
import numpy as np
from numpy import *
from numpy import pi
from numpy import array  # массив
from scipy import special  # jy_zeros/jnyn_zeros
from numpy import arange  # как range, но с шагом типа float
from numpy import degrees  # Преобразует радианную меру угла в градусную.
from numpy import radians  # Преобразует градусную меру угла в радианную.
from numpy import sin, cos, tan, arcsin, arccos, arctan, sinh, cosh, tanh, arcsinh, arccosh, arctanh
from charting_module import charting_module
from support_functions import *

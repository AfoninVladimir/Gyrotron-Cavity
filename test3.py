# import sympy
from sympy import *

x = symbols('x')
expr = sin(x)

# Use sympy.lambdify() method
f = lambdify(x, expr, "math")

print("Using lambda function in SymPy to evaluate sin(90) : {}".format(f(90)))

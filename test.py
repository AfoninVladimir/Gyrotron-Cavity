import numpy as np
from numpy import cos, sin, tan  # Входной массив в радианах.
from numpy import degrees  # Преобразует радианную меру угла в градусную.
from numpy import radians  # Преобразует градусную меру угла в радианную.

mm = 10**(-3)
R0 = 3.47 * mm

L1 = 10. * mm
L2 = 11. * mm
L3 = 12. * mm
LLW = 5. * mm
LRW = 5. * mm

zleft = -(L1 + LLW)
zright = (L2 + L3 + LRW)
zstr = 0.0 * mm
zfin = L2

# print(zleft, zright)
# print(zstr, zfin)

alphal = radians(-5.0)
alphar = radians(3.0)


z1 = -(LLW + L1)
z2 = -L1
z3 = 0.0 * mm
z4 = L2
z5 = L2 + L3
z6 = L2 + L3 + LRW

# print("z1", z1)
# print("z2", z2)
# print("z3", z3)
# print("z4", z4)
# print("z5", z5)
# print("z6", z6)
print()
n = 18  #18
R1 = round(R0 + tan(alphal) * (z3 - z2), n)
R2 = round(R0 + tan(alphal) * (z3 - z2), n)
R3 = round(R0, n)
R4 = round(R0, n)
R5 = round(R0 + tan(alphar) * (z5 - z4), n)
R6 = round(R0 + tan(alphar) * (z5 - z4), n)

# print("R1", round(R1, 18))
# print("R2", round(R2, 18))
# print("R3", round(R3, 18))
# print("R4", round(R4, 18))
# print("R5", round(R5, 18))
# print("R6", round(R6, 18))

# print("z < z1, R1")
# print("z1 <= z < z2, R1 + (z - z1) * (R2 - R1)/(z2 - z1)")
# print("z2 <= z < z3, R2 + (z - z2) * (R3 - R2)/(z3 - z2)")
# print("z3 <= z < z4, R3 + (z - z3) * (R4 - R3)/(z4 - z3)")
# print("z4 <= z < z5, R4 + (z - z4) * (R5 - R4)/(z5 - z4)")
# print("z5 <= z < z6, R5 + (z - z5) * (R6 - R5)/(z6 - z5)")
# print("z >= z6, R6")

print()

# print(f"z < {z1}, {R1}")
# print(f"{z1} <= z < {z2}, {R1} + (z - ({z1})) * ({R2} - {R1})/({z2} - ({z1}))")
# print(f"{z2} <= z < {z3}, {R2} + (z - ({z2})) * ({R3} - {R2})/({z3} - ({z2}))")
# print(f"{z3} <= z < {z4}, {R3} + (z - {z3}) * ({R4} - {R3})/({z4} - {z3})")
# print(f"{z4} <= z < {z5}, {R4} + (z - {z4}) * ({R5} - {R4})/({z5} - {z4})")
# print(f"{z5} <= z < {z6}, {R5} + (z - {z5}) * ({R6} - {R5})/({z6} - {z5})")
# print(f"z >= {z6}, {R6}")

print(f"z <= {-31.5 * mm}, {11. * mm}")
print(f"{-31.5 * mm} < z < {-24.0 * mm}, (11. + (19.736 - 11) * (z / {mm} - (-31.5)) / 7.5) * {mm}")
print(f"{-24.0 * mm} <= z <= {-23.0 * mm}, {19.736 * mm}")
print(f"{-23 * mm} < z < {-12 * mm}, (-38.23014642003139 + np.sqrt(3481. - (12.0 + z/{mm}) ** 2)) * {mm}")
print(f"{-12. * mm} <= z <= {0 * mm}, {20.77 * mm}")
print(f"{0.0 * mm} < z <= {17.7873 * mm}, (295.7702855739705 -  np.sqrt(75625.0 - (0.0 + z/{mm}) ** 2)) * {mm}")
print(f"{17.7873 * mm} < z < {80.0 * mm}, (-938.4552895706714 + np.sqrt(925090.40258244 - (-80.0 + z/{mm}) ** 2)) * {mm}")
print(f"{80 * mm} <= z, {23.36 * mm}")


"x <= -31.5 * mm,                   11.* mm "
"31.5 * mm < x < -24.0 * mm,        (11. + (19.736 - 11) (x/mm - (-31.5))/7.5) * mm"
"-24.0 * mm <= x <= -23.0 * mm,     19.736 mm"
"-23 * mm < x < -12 * mm,           (-38.23014642003139 + Sqrt[3481. - (12. + x/mm)^2]) * mm"
"-12. * mm <= x <= 0 *  mm,         20.77 mm"
"0.0 * mm < x <= 17.7873 * mm,      (295.7702855739705 - Sqrt[75625. - (0. + x/mm)^2]) * mm"
"17.7873 * mm < x < 80.0 * mm,      (-938.4552895706714 + Sqrt[925090.40258244 - (-80. + x/mm)^2]) * mm"
"80 * mm <= x,                      23.36 * mm"

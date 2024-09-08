###
# Reformat th equations from the wolfram export to a python string that can be evaluated

import math

file = open("text files/raw_psi.txt", "r")
string: str = [line for line in file][0]
x_distance: float = -0.00276
x_velocity: float = 0.221219613
x_acceleration: float = 0
y_distance: float = 0.007986354
y_velocity: float = 0.13
y_acceleration: float = 0
phi_distance: float = -0.463758745
phi_velocity: float = 0.245535084
phi_acceleration: float = 0
psi_distance: float = 0
psi_velocity: float = 12.58138277
psi_acceleration: float = 0
ramp_angle: float = 0.5
ahead: float = 0.0149
bhead: float = 0.00867
atail: float = 0.0251
btail: float = 0.00385
mhead: float = 0.0115
mtail: float = 0.0068
phi_inertia: float = 3.63 * (10 ^ -6)
psi_inertia: float = 1.87 * (10 ^ -7)
g: float = 9.81
friction_coefficient: float = 0.3095
# Replace everything
replacements = {"Ï•[t]": "phi_distance", "x[t]": "x_distance", "y[t]": "y_distance", "Ïˆ[t]": "psi_distance",
                "Derivative[1][x][t]": "x_velocity", "Derivative[1][y][t]": "y_velocity",
                "Derivative[1][Ï•][t]": "phi_velocity", "Derivative[1][Ïˆ][t]": "psi_velocity",
                "Derivative[2][x][t]": "x_acceleration", "Derivative[2][y][t]": "y_acceleration",
                "Derivative[2][Ï•][t]": "phi_acceleration", "Derivative[2][Ïˆ][t]": "psi_acceleration",
                "Î¸ramp": "ramp_angle", "Î¼": "friction_coefficient", "[": "(", "]": ")",
                "ArcSin": "math.asin", "ArcCos": "math.acos", "Sin": "math.sin", "Cos": "math.cos", "Sqrt": "math.sqrt",
                "^": "**"}
for variable in replacements.keys():
    string = string.replace(variable, replacements[variable])
try:
    test = eval(string)
    new_file = open("text files/psi_acceleration.txt", "w")
    new_file.write(string)
except ZeroDivisionError:
    print("zero division error broke")

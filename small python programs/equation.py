'''
Try to solve this equation (try find 1 of roots) 
3x^3 - 4x^2 + 9x +5 = 0 
Here ^ means exponent
'''

import math

print("Solving equation: 3x^3 - 4x^2 + 9x + 5 = 0")

a = 3
b = -4
c = 9
d = 5

x = 0

p = (-b/(3*a))
q = ((p**3) + (b*c-3*a*d)/(6*a**2))
r = (c / (3*a))

parentheses = (r - p ** 2)**3
brackets = math.pow(q**2 + parentheses, (1/2))
curly_brackets1 = math.pow(q + brackets, (1/3)) 
negative_number = q - brackets

curly_brackets2 = -math.pow(-negative_number, (1/3)) 


x = curly_brackets1 + curly_brackets2 + p

print(x)

# THIS CALCULATES THE SAME BUT FORMULA IS MUCH LONGER

# part1 = (((-b**3) / (27*a**3)) + ((b*c) / (6*a**2)) - (d / (2*a)))
# part2 = ((((-b**3) / (27*a**3)) + ((b*c) / (6*a**2)) - (d / (2*a)))**2)
# part3 = (((c / (3*a)) - ((b**2) / (9*a**2)))**3)

# square_root = math.sqrt(part2 + part3)
# print(f"square root: {square_root}")

# formula_part1 = part1 + square_root
# print(f"formula part 1: {formula_part1}")

# cubic_root1 = math.pow(formula_part1, (1/3))
# print(f"cubic root 1: {cubic_root1}")

# formula_part2 = part1 - square_root
# print(f"formula part 2: {formula_part2}")

# cubic_root2 = -math.pow(-formula_part2, (1/3))
# print(f"cubic root 2: {cubic_root2}")

# formula_part4 = (b / (3*a))

# x = cubic_root1 + cubic_root2 - formula_part4

# print(f"x is {x}")
'''
Program calculates the exponential value (base and exponent are given invariable). Base can be a real number, exponent is a whole number. Use a loop.
'''

base = float(input("Give a number (base): \n"))
exponent = int(input("Give another number (exponent):\n"))

# math = base ** exponent

times = 1
multiplication = base

while times < exponent:
    times = times + 1
    multiplication = multiplication * base

print(f"Exponential value when {base} is the base and {exponent} is the exponent: {multiplication}")
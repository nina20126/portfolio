'''
Calculates amount of combinations (try to use also an own factorial function here).
'''

from func_factorial import calculate_factorial

print("This program calculates amount of combinations.")

n = int(input("Insert n:\n"))
k = int(input("Insert k:\n"))

combinations = calculate_factorial(n) / (calculate_factorial(k) * calculate_factorial(n - k))

print(f"Amount of combinations is: {combinations}")
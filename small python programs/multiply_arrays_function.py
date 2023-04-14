'''
Create a function that multiplies two arrays.
'''

import random

random_array = []
random_array2 = []

while len(random_array) < 10:
    random_number = random.randint(0, 100)
    random_number2 = random.randint(0, 100)
    random_array.append(random_number)
    random_array2.append(random_number2)

print(f"Array 1: {random_array}")
print(f"Array 2: {random_array2}")

def multiply_arrays(arr1, arr2):
    multiplied = [a * b for a, b in zip(arr1, arr2)]

    return multiplied

new_array = multiply_arrays(random_array, random_array2)
print(f"Multiplied array: {new_array}")
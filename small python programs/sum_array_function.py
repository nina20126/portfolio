'''
Returns the sum of an array.
'''

import random

random_numbers = []

for i in range(30):
    random_numbers.append(random.randint(0,100))

def sum_array(array):
    sum = 0
    for i in array:
        sum += i
    return sum

sum = sum_array(random_numbers)

print(f"Random numbers: {random_numbers}")

print(f"sum: {sum}")
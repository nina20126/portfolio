'''
Array contains 30 random values. Calculate the sum and average.
'''

import random

values = []
sum = 0

for i in range(30):
    values.append(random.randint(0,100))
    sum += values[i]

average = sum / len(values)

print(f"The values are:{values}")

print(f"The sum of these values is: {sum}")

print(f"Averge of these values is: {average}")
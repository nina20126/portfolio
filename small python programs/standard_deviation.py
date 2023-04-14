'''
There are 20 values in an array: calculate the standard deviation
'''

import random
import math

random_numbers = []
deviation_array = [] # poikkeamat
deviation_square = [] # poikkeaman neliö

number = 0 # random number
sum_random_numbers = 0
average = 0
deviation = 0
square = 0
sum_of_squares = 0

# määrittää satunnaisen lukujonon, 20 lukua
while len(random_numbers) < 20:
    number = random.randint(0, 100)
    random_numbers.append(number)

print(random_numbers)

# lasketaan random_numbers lukujen summa
for i in random_numbers:
    sum_random_numbers = sum_random_numbers + i

# lasketaan random_numbers lukujen keskiarvo
average = sum_random_numbers / len(random_numbers)

# määritetään lista poikkeamista
for i in random_numbers:
    deviation = i - average
    deviation_array.append(deviation)
    
# poikkeaman neliö
for i in deviation_array:
    square = i ** 2
    deviation_square.append(square)

# neliöiden summa
for i in deviation_square:
    sum_of_squares = sum_of_squares + i

variance= sum_of_squares / (len(random_numbers) - 1)
standard_deviation = math.sqrt(variance)

print(f"Standard deviation: {standard_deviation}")
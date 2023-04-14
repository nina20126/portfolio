'''
Calculates the standard deviation.
'''

import math

try:
    user_list = []

    while True:
        user_list.append(int(input("Add a number:")))

except:
    print(user_list)

def standard_deviation(list_of_numbers):
    deviation_array = [] # poikkeamat
    deviation_square = [] # poikkeaman neliö

    user_list_sum = 0
    average = 0
    deviation = 0
    square = 0
    sum_of_squares = 0


    # lasketaan lukujen summa (user_list)
    for i in user_list:
        user_list_sum = user_list_sum + i

    # lasketaan keskiarvo (user_list)
    average = user_list_sum / len(user_list)

    # määritetään lista poikkeamista
    for i in user_list:
        deviation = i - average
        deviation_array.append(deviation)
        
    # poikkeaman neliö
    for i in deviation_array:
        square = i ** 2
        deviation_square.append(square)

    # neliöiden summa
    for i in deviation_square:
        sum_of_squares = sum_of_squares + i

    variance= sum_of_squares / (len(user_list) - 1)
    standard_deviation = math.sqrt(variance)

    return standard_deviation

result = standard_deviation(user_list)

print(result)
'''
Generate a lottorow (try to use an array here).
'''

import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

lottorow = []

while len(lottorow) < 7:
    random_number = random.choice(numbers)
    lottorow.append(random_number)
    numbers.remove(random_number)

lottorow.sort()
print(lottorow)
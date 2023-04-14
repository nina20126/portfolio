'''
Searches for a value from an array.
'''

import random
from square_root_function import square_root

random_numbers = []

while len(random_numbers) < 30:
    number = random.randint(0, 100)
    random_numbers.append(number)

def seach_value(arr, num):
    try:
        number_found = arr.index(num)
        return f"Number {num} found in index:{number_found}"

    except:
        return "Not found on the list"
        

search_number = int(input("Type number between 0 - 100:\n"))

result = seach_value(random_numbers, search_number)
square = square_root(random_numbers)

print(result)
print(random_numbers)
print(f" Square root: {square}")
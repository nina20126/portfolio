'''
Search a value from an array
'''

import random

values = []
searching_for = int(input("What number you are searching for?\n"))
result = f"{searching_for} is not in the list."

for i in range(30):
    values.append(random.randint(0,100))
    if values[i] == searching_for:
        result = f"{searching_for} found in position {i}"
        break

print(f"The values are:{values}")
print(result)
'''
Find the maximun of an array.
'''
import random

values = []
max = 0 

for i in range(30):
    values.append(random.randint(0,100))
    if values[i] > max:
        max = values[i]

print(f"The values are:{values}")
print(f"The maximum value is: {max}")
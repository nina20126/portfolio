'''
Create a function that sorts an array by using selection sort.
'''

import random

random_array = []

while len(random_array) < 20:
    random_number = random.randint(0, 10000)
    random_array.append(random_number)

print(f"Array before selection sort: {random_array}")

def selectionSort(array):
    lenght = len(array)

    for i in range(lenght - 1):
        min_index = i

        for j in range(i + 1, lenght):
            if array[j] < array[min_index]:
                min_index = j

        (array[i], array[min_index]) = (array[min_index], array[i])
    
    return array

selectionSort(random_array)
print(f"Array after selection sort: {random_array}")
'''
Program throws dice 100 times and tells amounts of different values (1, 2, 3, 4, 5, and 6).
'''

import random

dice = random.randint(1,6)
sum = 0
throw = 1

while throw < 100:
    print(f"This is throw number {throw}")
    throw = throw + 1
    sum = sum + dice
    print(f"Dice: {dice}")
    print(f"The sum is now {sum}\n")
    dice = random.randint(1,6)

print(f"\nFINAL: The sum is {sum}")
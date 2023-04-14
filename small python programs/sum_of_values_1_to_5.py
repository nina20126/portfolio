'''
Program calculates the sum of values 1 - 5. Use: for and while
'''

print("First we calculate the sum of values 1 - 5 using for-loop.")

sum = 0

for x in range(6):
    sum = sum + x
print("Calculating....")
print(f"1 + 2 + 3 + 4 + 5 = {sum}\n")

print("And then the same operation using while-loop!\n")

sum2 = 0
x = 0

while x < 5:
    x = x + 1
    sum2 = sum2 + x

print("Calculating....")
print(f"1 + 2 + 3 + 4 + 5 = {sum2}")
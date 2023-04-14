'''
Program calculates sum: 5, 10, 15, .. 100. Use: for and while
'''

print("What would be the sum of numbers 5, 10, 15 .... 100? Let's find out using for-loop")
sum = 0
for x in range(5, 105, 5):
    sum = sum + x

print("Calculating...")
print(f"The sum is {sum}\n")  

print("And this is how we do the same using while-loop")

sum2 = 0
x = 0

while x < 100:
    x = x + 5
    sum2 = sum2 + x

print("Calculating...")
print(f"The sum is {sum2}")

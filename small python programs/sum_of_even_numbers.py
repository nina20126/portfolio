'''
Program calculates the sum of even numbers between 2 - 40. Use: for and while
'''

print("Let's calculate the sum of even numbers between 2 and 40.")
print("First we do the math using for-loop!")

sum = 0

for x in range(2, 42, 2):
    sum = sum + x
    
print("Calculating....")
print(f"The sum is {sum}\n")

print("And then again the same with while-loop!")

sum2 = 0
x = 0

while x < 40:
    x = x + 2
    sum2 = sum2 + x

print("Calculating....")
print(f"And we get {sum2}")
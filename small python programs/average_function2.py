'''
Returns the average of 4 floating point values.
'''

def average(a, b, c ,d):
    average = (a + b + c + d) / 4
    return average

num1 = float(input("Give a decimal number:\n"))
num2 = float(input("Give a decimal number:\n"))
num3 = float(input("Give a decimal number:\n"))
num4 = float(input("Give a decimal number:\n"))

result = average(num1, num2, num3, num4)
print(f"Average of 4 numbers that you choosed: {result}")

a = 1.5
b = 0.222
c = 5.00001
d = 10.0

result = average(a, b, c, d)
print(f"Average of 4 decimal numbers that I choosed: {result}")
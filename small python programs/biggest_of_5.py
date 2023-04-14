'''
Function returns the biggest of 5 integers
'''

a = int(input("Give a number:"))
b = int(input("Give a number:"))
c = int(input("Give a number:"))
d = int(input("Give a number:"))
e = int(input("Give a number:"))


def find_biggest(num1, num2, num3, num4, num5):
    if num1 >= num2 and num1 >= num3 and num1 >= num4 and num1 >= num5:
        return num1
    elif num2 >= num1 and num2 >= num3 and num2 >= num4 and num2 >= num5:
        return num2 
    elif num3 >= num1 and num3 >= num2 and num3 >= num4 and num3 >= num5:
        return num3 
    elif num4 >= num1 and num4 >= num2 and num4 >= num3 and num4 >= num5:
        return num4
    else:
        return num5

biggest_of_5 = find_biggest(a, b, c, d, e)

print(f"The biggest number is: {biggest_of_5}")
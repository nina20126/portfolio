'''
Returns the biggest of 3 integers.
'''

a = int(input("Give a number:"))
b = int(input("Give a number:"))
c = int(input("Give a number:"))


def find_biggest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

biggest_of_3 = find_biggest(a, b, c)

print(f"The biggest number is: {biggest_of_3}")
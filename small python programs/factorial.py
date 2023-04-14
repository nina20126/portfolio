'''
Program calculates the factorial of n (given in a variable)
'''

# factorial n! = n * (n - 1) * (n - 2) * (n - 3) * ...* 3 * 2 * 1
# for example: 5! = 5 * 4! = 5 * 4 * 3 * 2 * 1 = 120

user_number = int(input("Give a number: \n"))

changing_number = user_number
factorial = user_number

if user_number == 0:
    print("Factorial for 0 is 1")

while changing_number > 1 and user_number > 0:
    changing_number = changing_number - 1
    factorial = factorial * changing_number

if factorial > 0:
    print(f"Factorial for {user_number} is {factorial}")

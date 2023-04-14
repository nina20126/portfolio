'''
Returns the factorial.
'''
# factorial n! = n * (n - 1) * (n - 2) * (n - 3) * ...* 3 * 2 * 1
# for example: 5! = 5 * 4! = 5 * 4 * 3 * 2 * 1 = 120

def calculate_factorial(num):
    factorial = num

    if num == 0:
        factorial == 1

    elif num > 0:
        while num > 1:
            num = num - 1
            factorial = factorial * num
    
    else:
        factorial = "negative numbers doesn't have factorial"

    return factorial

if __name__ == '__main__':
    user_number = int(input("Give a number: \n"))

    return_factorial = calculate_factorial(user_number)
    print(f"Factorial is: {return_factorial}")
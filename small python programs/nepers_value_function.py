'''
Calculates an approximation of Neper's value (e).
'''

from func_factorial import calculate_factorial

n = int(input("Number of terms: "))

def find_e(num):
    sum = 1

    for i in range(1, num + 1):
        sum = sum + (1 / calculate_factorial(i))
    
    return f"e = {sum}"
    
e = find_e(n)
print(e)
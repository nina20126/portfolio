'''
Calculates approximations of sin(x) and cos(x)
'''

from func_factorial import calculate_factorial
import math

#sin(x)
pi = math.pi

def sin(x, n):
    sine=0
    for i in range(n):
        sign=calculate_factorial(-1, i)
        a=x*(pi/180)
        sine=sine+(sign*(a**(2.0*i+1))/calculate_factorial(2*i+1))
    return sine

x=int(input("Enter the value of x in degrees: "))
n=int(input("Enter the number of terms: "))
approximation = sin(x, n)
print(approximation)

#cos(x)
def cosine(x,n):
    cosx = 1
    sign = -1
    for i in range(2, n, 2):
        y=x*(pi/180)
        cosx = cosx + (sign*(y**i))/calculate_factorial(i)
        sign = -sign
    return cosx
x=int(input("Enter the value of x in degrees:"))
n=int(input("Enter the number of terms:"))
print(round(cosine(x,n),2))
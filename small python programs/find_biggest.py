'''
Variables a, b and c have different values. Create a program that finds the biggest one. Show 3 different ways to solve the problem.
'''

a = int(input("Give a number:"))
b = int(input("Give a number:"))
c = int(input("Give a number:"))

# 1
if a >= b and a >= c:
    print(f"{a} is the biggest number.")
elif b >= a and b >= c:
    print(f"{b} is the biggest number.")
else:
    print(f"{c} is the biggest number.")

# 2
if a > b:
    if a > c:
        print(f"{a} is the biggest number.")
    else:
        print(f"{c} is the biggest number.")
elif b > a:
    if b > c:
        print(f"{b} is the biggest number.")
    else:
        print(f"{c} is the biggest number.")
else:
    print(f"{c} is the biggest number.")

# 3
print(max(a, b, c), "is the biggest number.")
'''
User gives the lengths of the triangle's sides. Program tells what is the triangle like (e.g. is it right angled, isosceles…)
'''

side_A = float(input("Length of side A:"))
side_B = float(input("Length of side B:"))
side_C = float(input("Length of side C:"))

side_A_square = side_A ** 2
side_B_square = side_B ** 2
side_C_square = side_C ** 2

if (side_A + side_B) > side_C:
    # Right angled a2 + b2 = c2
    if side_A_square + side_B_square == side_C_square or side_B_square + side_C_square == side_A_square or side_A_square + side_C_square == side_B_square:
        print("Your triangle is right angled")

    # isosceles
    if side_A == side_B != side_C or side_A == side_C != side_B or side_C == side_B != side_A:
        print("Your triangle is isosceles")

    # equilaterial
    if side_A == side_B == side_C:
        print("Your triangle is equilaterial")

    # acute or obtuse? a2 + b2 > c2
    if side_A_square + side_B_square > side_C_square or side_A_square + side_C_square > side_B_square or side_B_square + side_C_square > side_A_square:
        print("Your triangle is acute")
    else:
        print("Your triangle is obtuse")
else:
    print("This is not a tringle.")
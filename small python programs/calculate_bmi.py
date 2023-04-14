'''
program calculates BMI
'''
height = int(input("Give your height in centimeters:"))
weight = int(input("Give your weight in kilos:"))

height_meters = height / 100

bmi = round(weight / (height_meters ** 2), 1)

print(f"Your BMI is: {bmi}")

if bmi < 18.5:
    print("You're in the underweight range")
elif bmi <= 24.9:
    print("You're in the healthy weight range")
elif bmi <= 29.9:
    print("You're in the overweight range")
else:
    print("You're in the obese range")
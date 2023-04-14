'''
Returns the BMI
'''

height_cm = int(input("Give your height in centimeters:"))
weight = int(input("Give your weight in kilos:"))

height = height_cm / 100

def bmi(weight, height):
    bmi = round(weight / (height ** 2), 1)

    if bmi < 18.5:
        return f"Your bmi is {bmi}. You're in the underweight range"
    elif bmi <= 24.9:
        return f"Your bmi is {bmi}. You're in the healthy weight range"
    elif bmi <= 29.9:
        return f"Your bmi is {bmi}. You're in the overweight range"
    else:
        return f"Your bmi is {bmi}. You're in the obese range"

my_bmi = bmi(weight, height)
print(my_bmi)
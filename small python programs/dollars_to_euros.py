'''
Create a euro converter: dollars to euro
'''

print("Convert dollars to euros")

dollars = float(input("Dollars:"))

# 1 dollar = 0.918696 euros 26 Jan 2023

euros = dollars * 0.918696

dollars = round(dollars, 2)
euros = round(euros, 2)

print(f"{dollars} dollars = {euros} euros")
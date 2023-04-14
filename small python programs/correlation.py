'''
2 arrays contain students grades in math and in English language. There are 10 students. Try to calculate the correlation
'''

import math 

math_grade_x = [8, 6, 9, 10, 10, 5, 8, 7, 6, 9]
english_grade_y = [6, 10, 9, 7, 8, 7, 5, 10, 10, 10]

x2 = []
y2 = []

for i in math_grade_x:
    i = i ** 2
    x2.append(i)

for i in english_grade_y:
    i = i ** 2
    y2.append(i)

xy = [math_grade_x[i]*english_grade_y[i] for i in range(len(math_grade_x))]
print(xy)

sum_xy = 0
sum_math_x = 0
sum_english_y = 0
sum_x2 = 0
sum_y2 = 0
n = 10 # sample size

for i in xy:
    sum_xy = sum_xy + i

for i in math_grade_x:
    sum_math_x = sum_math_x + i

for i in english_grade_y:
    sum_english_y = sum_english_y + i

for i in x2:
    sum_x2 = sum_x2 + i

for i in y2:
    sum_y2 = sum_y2 + i


formula= (n * sum_xy - sum_math_x * sum_english_y) / math.sqrt(( n * sum_x2 - (sum_math_x ** 2)) * (n * sum_y2 - (sum_english_y ** 2)))

print(formula)
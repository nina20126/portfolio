'''
Fill 2 arrays with some values and calculate the sum array.
'''

ar1 = [34, 44, 653, 45, 2, 5]
ar2 = [123, 44, 6, 91, 20, 1]

sum_array = [ar1[i] + ar2[i] for i in range(len(ar1))]

print(sum_array)
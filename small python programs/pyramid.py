'''
Print this kind of semipyramid (character amount of rows is given in a variable)
m 
mm 
mmm 
mmmm 
mmmmm
'''

rows = int(input("How many rows?\n"))

for i in range(rows):
    for j in range(i+1):
        print("m ", end="")
    print("\r")
'''
Create a short dictionary: e.g Finnish to English. Add some wordpairs to a list.
'''

dictionary = [["cat", "kissa"], ["dog", "koira"], ["mouse", "hiiri"], ["elephant", "norsu"], ["guinea pig", "marsu"], ["parrot", "papukaija"], ["gold fish", "kultakala"], ["horse", "hevonen"], ["cow", "lehmä"], ["sheep", "lammas"], ["bird", "lintu"], ["bunny", "pupu"], ["fox", "kettu"], ["elk", "hirvi"], ["reindeer", "poro"]]

print("There are some common animals listed on this dictionary.")
animal = input("Search for an animal: \n").lower()
result = f"Couldn't found {animal} in the dictionary"

for i in range(len(dictionary)):
    for j in range(len(dictionary[i])):
        if animal == dictionary[i][j]:
            result = f"Translation: {dictionary[i]}"

print(result)
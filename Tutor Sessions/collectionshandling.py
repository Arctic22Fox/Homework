# string with an item/value
string = 'Norwegian Blue', 'Mr. Khans Bike'
# collections
fruit = ['Banana', 'Apple', 'Guava', 'Orange']
numberlist = [1, 2, 3, 4, 5]

tuple = (47, 'Spam', 'Major', 683, 'Ovine Aviation')

# arithmetic operations on lists
print('min:',min(numberlist))
print('max:',max(numberlist))
print('sum:',sum(numberlist))

# accessing individual items using their indexes
print(numberlist[0])
print(numberlist[3])

# length of the list
print('Length of the list is', len(numberlist))

# return a range of items from a list - start index (included) to end index (excluded)
print(numberlist[1:3])

# items from begining of the list to a position
print(numberlist[:3])
print(numberlist[3:])

# change items
numberlist[0]=90
numberlist[3:]=[50,50]
print(numberlist)

# add items to a list
fruit += ['Mango', 'Pineapple']
print(fruit)

# remove items
fruit.remove('Mango')
print(fruit)

# iterate or loop over our list
for fruit in fruit:
    print(fruit)

# occurence of items in a list
count = fruit.count('Pineapple')
print('Pineapples occur ', count, ' time(s)')

# find the index of an item
fruit.index('Pineapple')

# find the index of a non-existing item
# fruit.index('car')

# sort list items
# fruit.sort()
# print(fruit)
# fruit.sort(reverse=True)
# print(fruit)

# dictionaries
mydict={'Australia':'Canberra','Eire':'Dublin','France':'Paris'}
print(mydict['Australia'])

country = 'Iceland'
mydict[country]='Reykjavik'

print(mydict['Iceland'])

# dictionary sorting an object of a type list
mydict2 = {'UK':['London','Liverpool','Manchester'], 'US':['Miami', 'New York', 'Bosotn']}
print(mydict2['UK'][2])

mydict2['FR'] = ['Paris', 'Lyon', 'Bordeaux']
print(mydict2['FR'][2])

# a loop to print the items
for item in mydict2:
    print(mydict2[item])

# breakout session: Collections
foods = ['Pizza', 'Kebab', 'Burger', 'Chips', 'Salad', 'Chocolate']
most_letters = 0
most_letters_item = None
for letters in foods:
    if len(letters) > most_letters:
        most_letters = len(letters)
        most_letters_item = letters
print(most_letters_item)
print(most_letters)

# Handling

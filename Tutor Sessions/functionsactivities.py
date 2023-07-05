import re

def rectangle(length, width):
    area = length * width
    return area

print(rectangle(10, 7))

def odd(num):
    if num % 2 != 0:
        return 'odd'
    else:
        return 'even'

print(odd(6))
print(odd(7))

def count(word):
    count_word = 0
    for x in word:
        if x in word:
            count_word += 1
            return count_word

string = "Hello World"
count = string.count("Hello")
print(count)


def count_words(string):
    string = string.replace(',', ' ')
    words = string.split()
    # creates a dictionary with key pairs to show the word in the sentence with the freq next to it
    countup={i:words.count(i) for i in words}
    for x, l in countup.items():
        print(x, ' is in the sentence ', l, ' times.')
count_words('the quick, brown fox, jumps over, the fence!')

def count_words(string):
    words = re.findall(r'\w+', string)
    # creates a dictionary with key pairs to show the word in the sentance with the freq next to it
    countup={i:words.count(i) for i in words}
    for x, l in countup.items():
        print(x, ' is in the sentance ', l, ' times.')
count_words('the quick, brown fox, jumps over, the fence!')
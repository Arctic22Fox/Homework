# Question 1: what is wrong with this?
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += 'Oke'
# Answer, this will add the OKE to the end of this tuple. the += operator is an addition, this string should read: ['Cheddar', 'Stilton', 'Cornish Yarg', 'O', 'k', 'e']
print(cheese)

# Question 2: what is going on here? can you explain the output?
tup = 'Hello'
print(len(tup))
# this print function is counting the length of the tuple and output the length of the word,  5 letter

tup = 'Hello',
print(len(tup))
# witht he addition of the , this is now counting the amount of words within the tuple, below is I add more words it, it should print how many words there are

tup = 'Hello', 'world', 'nice', 'to', 'meet', 'you'
print(len(tup))
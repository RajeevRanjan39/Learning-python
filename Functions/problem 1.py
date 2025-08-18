# write a python code using finction which calculates the number of case letters, lower case letters, total number of characters and numbers of words

def upper(s):
    upper=0
    for char in s:
        if(char.isupper()):
            upper+=1
    return upper

def lower(s):
    lower=0
    for char in s:
        if(char.islower()):
            lower+=1
    return lower

def characters(s):
    letters=0
    for char in s:
        letters+=1
    return letters

def words(s):
    word = 1
    for char in s:
        if(char == ' '):
            word += 1
    return word

sentence = input("Enter a sentence:")
uletters=upper(sentence)
Lletters=lower(sentence)
total=characters(sentence)
words = words(sentence)

print(f'\nTotal number of upper case characters: {uletters}')
print(f'\nTotal number of lower case characters: {Lletters}')
print(f'\nTotal number of character: {total}')
print(f'\nTotal number of words: {words}')

'''
Upper Case Only Vowels
Write a program that takes a passage with n lines of text as input. For each line or  convert all vowels (a or  e or  i or  o or  u) to uppercase and all other characters to lowercase.

NOTE: This is an I/O type question or  you need to write the whole code for taking input and printing the output.

Input Format

    • The first line contains an integer n or  the number of lines.

    • The next n lines contain the passage.

Output Format

    • Print the passage with vowels in uppercase and all other characters in lowercase.

'''


n = int(input())
passage =[]

for x in range(n):
    lines = input()
    passage.append(lines)

vowels = 'aeiou'

for line in passage:
    new_line = ""
    for char in line:
        if char.lower() in vowels:
            new_line += char.upper()
        else:
            new_line += char.lower()
    print(new_line)

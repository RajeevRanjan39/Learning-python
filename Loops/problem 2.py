# Find the number of digit in given number

num = abs(int(input("Enter a number: ")))
digit = 0

# while(num>0):
#     num = num // 10
#     digit = digit + 1

while(num>0):
    num = int(num / 10)
    digit = digit + 1

# digit = 1
# while(num>9):
#     num = num // 10
#     digit = digit + 1
# print(digit)
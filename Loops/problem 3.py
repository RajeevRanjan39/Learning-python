# Reverse the digit in given number

num = int(input('Enter a number: '))
absNum = abs(num)

rev = absNum % 10
absNum = absNum // 10
while(absNum):
    r = absNum % 10
    absNum = absNum // 10
    rev = rev * 10 + r
if(num>=0):
    print(rev)
else:
    rev = -1 * rev
    print(rev)

# num = num % 10
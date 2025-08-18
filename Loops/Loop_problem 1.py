# Find all the prime less than entered number

num = int(input('Enter a number: '))

while(num != 0):
    for i in range(1,num):
        if(num % i != 0):
            count += 1
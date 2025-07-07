# check whether the given number is ends with 0 or 5 or any other numbers

print("Enter a number")
num = int(input())

# last_digit = num % 10
# if(last_digit == 0):
#     print("Ends with 0")
# elif(last_digit == 5):
#     print("Ends with 5")
# else:
#     print("Ends with other number")

if(num % 5== 0):
    if(num % 10 == 0):
        print("Ends with 0")
    else:
        print("Ends with 5")
else:
    print("Ends with onther number")
    
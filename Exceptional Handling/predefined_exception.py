a = int(input())
b = int(input())

# c = a / b # will give and error called "ZeroDivisionError": division by zero

# to avoid this we do following things

try:
    f = open('rajeev.txt', 'r')
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Invalid input, divisor can't be zero")
# This is for following code
# print(d)
except NameError:
    print("Variable not defined")
except FileNotFoundError:
    print('Invalid file name. Please check again')
except:
    print("Something went wrong")
finally:
    f.close()
    print("Finally block is also executed")
def my_function1():
    global x
    x=x*2
    print("Value of x in function 1",x)

def my_function2():
    global x
    x=x*3
    print("Value of x in function 2",x)

x=5
print("Value of x before funtion",x)
my_function1()
my_function2()
print("Value of x after function",x)
'''
def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    return x / y
'''
# Instead of creating function for one line of code that is return statement, we use lambda function which warks in same as fucntion works

add = lambda x, y : x + y
sub = lambda x, y : x - y
mul = lambda x, y : x * y
div = lambda x, y : x / y


print(add(10,20))
print(sub(10,20))
print(mul(10,20))
print(div(10,20))
print(type(add))
a = [10, 20, 30, 40, 50, 60]
b = [5, 10, 15, 20, 25, 30]

def sub( x, y):
    return x-y

c = map(sub,a,b)
print(list(c))
print(type(c))

# we are creating a new list with increament of 1 in list a

def incre(x):
    return x + 1
print(type(a))
a = map(incre, a)
print(type(a))
print(list(a))
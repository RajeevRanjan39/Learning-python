# in general we use map in filter function

import math

a = [25, -16, 9, 81, -100]

def square_root (x):
    return math.sqrt(x)

def is_positive(x):
    if(x>=0):
        return x
    
b = map(square_root, filter(is_positive, a))
print(list(b))
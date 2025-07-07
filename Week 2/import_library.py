# Import Maths library
'''
import math
print(math.log(10))
print(math.sqrt(4))
print(math.pow(10,3))
'''

#import random library
import random
# print(random.random())

# print(random.randrange(1,7))

dice1 = random.randrange(1,7)
dice2 = random.randrange(1,7)
total = dice1 + dice2
print("The sum of two dice is:",total)

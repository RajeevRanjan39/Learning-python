# method 2
'''
from calendar import*
print(month(2025,11))
'''

# Method 3
'''
from calendar import month
print(month(2025,12))

# we can't use other function from library in this method

print(calendar(2025))
'''

# Method 4 (Modified version of method 3)
'''
from calendar import month , calendar
print(month(2026,11))
print(calendar(2026))
'''

# Method 5
'''
import calendar as c
print(c.month(2025,12))
'''

# Method 6 [Modified version of 3 and 5]
from calendar import month as m
print(m(2025,2))
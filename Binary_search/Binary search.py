''' Check if a given element k is present in a list or not '''
def obvious_search(L,k):
    for x in L:
        if x == k:
            return 1

    return 0

# Code Verified

'''
Question: Can we write a piece of code that searches for a given element in the list L faster than the obvious algorithm (given above)
'''

def binary_search(L,k):
    '''
    This function is an alternative for the obvious. It does exactly same what is expected from the obvious_search, but in on efficient way. This is popularly callled the binary search.
    '''

    # considering 'L' is sorted here

    # we want to shrink my list
    # we will do that using a while loop 

    begin = 0 # first element in L . L[0]
    end = len(L) - 1 # the last element in L is in len(L) . L[len(l)-1]

    # use a while loop to look at the list and keep halving it
    while(end - begin > 1):
        # we will handle the case when the number of element is less than or equal to 1
        
        # compute the mid which is the mid point of begin to end.
        mid = (begin + end) // 2
        if L[mid] == k:
            return 1
        # if mid is indeed k, then we return True and stop the code.
        
        # if the middle element is greater than k, then cut the right side and retain the left side
        if L[mid] > k:
            # L = L[::len(l)/2]
            end = mid - 1
        
        # if the middle element is less than k, then cut the left side and retain the right side
        if (L[mid]<k):
            # L = L[(len(L)/2)::]
            begin = mid + 1

    '''
    If we are here it means that we have't found the element.
    or
    while condition is violated. Which means end - begin is less than 1 or equal

    '''

    # if it is equal to 1 , then there is exactly two element
    if L[begin] == k or L[end] == k :
        return 1
    else:
         return 0
    

L = list(range(1000*10000))
n = int(input("Enter"))

import time

a = time.time()
print(obvious_search(L,n))
b = time.time()
print(b-a)

a = time.time()
print(binary_search(L,n))
b = time.time()
print(b-a)
'''
In this piece of code to check if a given list has 0 in it or not. If has "zero" in it, we will return True(1) otherwise False(0)
'''

def check0(L):
    # if the list is empty, return False(0)
    if len(L)==0:
        return 0
    if L[0]==0:
        return 1
        # if the first element is zero then return 1
    else:
        return check0(L[1:len(L)])
        # this one will simply outsources
    

output = check0([1,2,3,4,5,6,7,3])
print(output)
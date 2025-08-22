
def min(L):
    # finds the minimum element in the list L
    mini=L[0]
    for x in L:
        if x<mini:
            mini = x
    return mini

def sort(L):
    # Recursively sort the list L
    if L==[] or len(L)==0:
        return L
    
    m = min(L)
    # m is now contains the minimum most element in L
    L.remove(m)
    # we remove that element from L
    return [m] + sort(L)
    # now we recursively the smaller list

L = [5,6,2,9, 23,53]
print(sort(L))
print(type(sort(L)))

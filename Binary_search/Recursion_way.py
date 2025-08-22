def rbinarysearch(L,k,begin,end):
    '''This will recursively compute binary search '''

    # If begin and end is same then just check L[begin]

    if(begin==end):
        if L[begin]==k:
            return 1
        else:
            return 0

    # If begin and end are consecutive, then check them individualy    
        if (end - begin == 1):
            if L[begin] == k or L[end] == k :
                return 1
            else:
                return 0
            


        # if end - begin  > 1:
        if end - begin  > 1:
            # compute the middle element
            mid = (begin + end) // 2
            if L[mid] > k:
                # discard the right and retain the left
                end = mid - 1
            if L[mid] < k:
                # discard the left and retain the right
                begin = mid + 1
            if L[mid] == k:
                return 1
        if end-begin < 0:
            return 0
            
        return rbinarysearch(L,k,begin,end)

# L = [2,6,9,11,26,58,78]
L = list(range(10000000))
r = rbinarysearch(L,2,0,len(L)-1)
print(r)
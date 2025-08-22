# function 
def sum(n):
# Verified
    ans = 0
    for i in range(n):
        ans = ans + (i+1)
    return ans

# Using Recursion
def sum2(n):
# Verified
    if n==1:
        return 1
    else:
        return n + sum2(n-1)


# compute compound interest by assumming the interest to be 10%

def comp(p,n):
# Verified
    if n == 1:
        return p * 1.1
    else:
        return 1.1 * comp(p,n-1)

def fact(n):
# Verified
    if n==1:
        return 1
    else:
        return n * fact(n-1)
    

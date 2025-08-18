# intialise c to 0
# I need to consider dot product of two matrices  A and B
# I need to pick ith row and jth column in a matrix

def intialise_mat(dim):
    C = []
    for i in range(dim):
        C.append([])
    for i in range(dim):
        for j in range(dim):
            C[i].append(0)
    return C

def dot_product(u,v):
    # letting we have same dimension of matices both
    dim=len(u)
    ans = 0
    for i in range(dim):
        ans+=u[i]*v[i]
        return ans
    
def row(M,i):
    dim=len(M)
    l=[]
    for k in range(dim):
        l.append(M[i][k])
    return l

def column(M,j):
    dim=len(M)
    l=[]
    for k in range(dim):
        l.append(M[k][j])
    return l

def mat_multi(A,B):
    dim=len(A) #Assuming A and B of same dimension and square matrix
    C=intialise_mat(dim)
    for i in range(dim):
        for j in range(dim):
            for k in range(dim):
                # C[i][j] = ith row of A * jth col of B
                C[i][j]+=A[i][k]*B[k][j]
    return C


A= [[1,2,3],[4,5,6],[7,8,9]]
B=[[1,2,1],[3,1,7],[6,2,3]]
print(mat_multi(A,B))
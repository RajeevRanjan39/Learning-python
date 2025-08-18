# find out the minimum most element in the list l
# append that to a new list x
# Remove the minimum  from original list l

# find out the minimum most element in the list l
def min_list(l):
    mini = l[0]
    for i in range(len(l)):
        if(mini>l[i]):
            mini=l[i]
    return mini

def sort_obvious1(l):
    x=[]
    while(len(l)>0):
        mini = min_list(l)
        l.remove(mini)
        x.append(mini)
    return x

# we are just learn that  dividing our problem into smaller parts and solving them 
# makes it easy on our hand

def sort_obvious(l):
    x=[]
    while(len(l)>0):
        mini = l[0]
        for i in range(len(l)):
            if(l[i]<mini):
                mini=l[i]
        x.append(mini)
        l.remove(mini)
    return x


l = [ 90,24,15,35,97,18,20,5,1]
print(sort_obvious1(l))
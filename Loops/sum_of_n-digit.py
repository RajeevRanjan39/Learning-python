# we are finding the sum of first n numbers
# In this code we are using only one parameter in range (for loop)

print("Enter a number")
n = int(input())
ans = 0 

for i in range(n):
    ans = ans + i
print("Sum of first", n-1, "number is:",ans)
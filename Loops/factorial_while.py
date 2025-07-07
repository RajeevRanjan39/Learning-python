print("Enter a number")
n=int(input())
answer = 1
# while(n!=0):
#     answer = answer * n
#     n= n-1

i = 1
while(i<=n):
    answer = answer * i
    i = i + 1
print(answer)
# WAP to check if a list contains paindrome of elements. (Hint: use copy() method)
# [1,2,3,3,2,1]

list = [1,2,3,2,1]


# list2 = list.copy()
# count = 0

# for i in range(5):
#     if(list[i] == list2[4-i]):
#         count +=1
#     else:
#         break
# if (count == 5):
#     print("palindrome")
# else:
#     print("Not a palindrome")

# this is not a ideal way of solving

list_copy = list.copy()
list_copy.reverse()

if (list == list_copy):
    print("palindrome")
else:
    print("Not a palindrome")



# Find the grade of student based on given marks from 0 to 100

print("Enter your marks")
marks = int(input())
# if(marks >= 0 and marks<=100):
#     if(marks>=90):
#         print("A")
#     if(marks>=80 and marks<90):
#         print("B")
#     if(marks>=70 and marks<80):
#         print("C")
#     if(marks>=60 and marks<70):
#         print("D")
#     if(marks<60):
#         print("E")
# else:
#     print("Invalid")

# using elif
if(marks >= 0 and marks<=100):
    if(marks>=90):
        print("A")
    elif(marks>=80):
        print("B")
    elif(marks>=70):
        print("C")
    elif(marks>=60):
        print("D")
    else:
        print("E")
else:
    print("Invalid")
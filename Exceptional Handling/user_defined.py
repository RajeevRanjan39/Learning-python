# in this piece of code we are creating error

a = int(input())
if a < 18:
    # instead of 
    # print("You are under age, you cannot drive")
    # use this to give an error message
    raise Exception("You are under age, you cannot drive")
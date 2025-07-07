print("when did india get its independence?(Year)")
year = int(input())

if(year == 1947):
    print("Hurray! You got it correct.")
else:
    print("Cemom, You don't know this Idoit?")
    print("That's ok! you have second chance.")
    print("when did india get its independence?(Year)")
    year = int(input())
    if(year == 1947):
        print("You are right now.")
    else:
        print("You failed in second attempt too? grrrr.....")

# we can see in this piece of code that we are doing same task for two time (Asking same question and taking input) for that we will use loop
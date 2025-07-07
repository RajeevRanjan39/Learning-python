# This is basic example of while loop , where we are asking a question "When did India get its independence(year)?"

print("When did India get its independence(year)?")
year = int(input())
while(year != 1947):
    print("You got it wrong. Enter again.")
    year = int(input())
print("Wowwww..... You got it right!")
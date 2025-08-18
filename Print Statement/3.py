# feature 3
# formating print statement in easier way

# table of 
num = int(input('Enter number:'))
for i in range(1,11):
    # print(num, "X", i, "=", num * i) # Normal way

    # print(f'{num} X {i} = {num * i}') 
    # print('{0} X {1} = {2}' .format(num, i, num * i))
    print('%d X %d = %d' %(num, i,num*i)) # Old way like C progg.
    # All will give same output

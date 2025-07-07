# Transform flowchart into python code

print('Travel from city A to city B')
time= int(input('Enter time:'))
longer = int(input('Define longer:'))
if(time >= longer):
    price = int(input('Enter price:'))
    higher = int(input('Define Higher:'))
    if(price>=higher):
        print("Train")
    else:
        print("Coach")
else:
    price = int(input('Enter price:'))
    higher = int(input('Define Higher:'))
    if(price>=higher):
        print("Daytime Flight")
    else:
        print("Red Eye flight")
print("Arrive city B")
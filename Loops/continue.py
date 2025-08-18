# Extracting username and domail name from email-id

mail = input('Enter your Email-id: ')

for char in mail:
    if (char == '@'):
        print('')
        continue
    print(char,end='')
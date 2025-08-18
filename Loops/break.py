# Example of Break statement

# Extracting username from email-id

id = input('Enter your email-id: ')
for char in id:
    if(char=='@'):
        break
    print(char , end = '')
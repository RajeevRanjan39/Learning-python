pi = 22/7
# Without format specifier
print("Without format specifier")
print(f'value of pi is {pi}')
print('value of pi is {0}' .format(pi))
print('value of pi is %f' %(pi))

# With format specifier
print("With format specifier")
print(f'value of pi is {pi:.2f}')
print('value of pi is {0:.2f}' .format(pi))
print('value of pi is %.2f' %(pi))

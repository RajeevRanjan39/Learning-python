'''
This program considers an input file by using caesar cipher. By that mean, we shift back the letters by 3 units. For example, d becomes a , e becomes b and so on 
'''

import string

def create_caesar_dictionary():
    l=string.ascii_lowercase
    l=list(l)

    d={}
    for i in range(len(l)):
        d[l[i]] = l[(i-3)%26]
    return d

f=open('encrypted_story.txt', 'r')
g=open('decrypted_story.txt', 'w')

d = create_caesar_dictionary()

c = f.read(1)
while(c!=''):
    g.write(d[c])
    c=f.read(1)

f.close()
g.close()

# Example of nested loop

s = 'VIBGROY'
t = 'VIBGROY'
count = 0
for i in range(7):
    for j in range(7):
        print(s[i],t[j])
        count += 1
print("Total number of combination is", count)
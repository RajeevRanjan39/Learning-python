malgudi = [
    'It', 'was', 'Monday', 'morning', 'Swaminathan', 'was', 'reluctant', 'Monday',
    'specially', 'unpleasant', 'in', 'the', 'calendar', 'After', 'the', 'delicious',
    'reluctant', 'to', 'open', 'his', 'eyes', 'he', 'considered', 'freedom', 'of',
    'Saturday', 'mood', 'of', 'work', 'and', 'dismal', 'yellow', 'building', 'and',
    'Sunday', 'it', 'was', 'difficult', 'to', 'get', 'discipline', 'He', 'shuddered',
    'at', 'the', 'very', 'fire-eyed', 'Vedanayagam', 'his', 'class', 'teacher',
    'and', 'headmaster', 'with', 'his', 'thin', 'long', 'face', 'to', 'get',
    'into', 'the', 'Monday', 'mood', 'the', 'very', 'thought', 'of', 'school',
    'the', 'dismal', 'cane'
]
s = set(malgudi)
d={}
for x in s:
    d[x] = 0
max= 0 
answer_word = ''
for x in malgudi:
    d[x] = d[x] + 1

for x in d:
    if max<d[x]:
        max = d[x]
        answer_word = x

print(d)
print(max)
print(answer_word)

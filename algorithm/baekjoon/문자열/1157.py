from collections import Counter
char = input()
upper_char = char.upper()
counter = Counter(upper_char).most_common()
if len(counter) > 1 and counter[0][1] == counter[1][1]:
    print('?')
else:
    print(counter[0][0])

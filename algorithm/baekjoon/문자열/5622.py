char = input()
dials = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
seconds = len(char)*3
for c in char:
    for i, dial in enumerate(dials):
        if c in dial:
            seconds += i
print(seconds)

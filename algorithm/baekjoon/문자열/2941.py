import re
char = input()
char = re.sub('c=|c-|dz=|d-|lj|nj|s=|z=', 'a', char)
print(len(char))

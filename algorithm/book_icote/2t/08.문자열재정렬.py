from curses.ascii import isalnum


def solution(s):
    char = []
    num = 0
    for c in s:
        if c.isnumeric():
            num += int(c)
        else:
            char.append(c)
    char.sort()
    return ''.join(char)+str(num)


print(solution('K1KA5CB7'))

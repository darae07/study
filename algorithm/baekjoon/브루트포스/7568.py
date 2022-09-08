# n =사람의 수
# 사람의 덩치 등수 = 자신보다 덩치가 큰 사람의 수 k+1
# k = 키와 몸무게 모두 큰 사람 수
# 완전탐색 - 자신과 모든 사람을 비교할 수밖에 없음

n = int(input())
people = []
rate_list = []
for _ in range(n):
    height, weight = map(int, input().split())
    people.append((height, weight))
for i, me in enumerate(people):
    my_rate = 1
    for j, other in enumerate(people):
        if i != j and other[0] > me[0] and other[1] > me[1]:
            my_rate += 1
    rate_list.append(my_rate)
print(' '.join(str(s) for s in rate_list))

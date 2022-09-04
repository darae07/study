# **풀이 설명
# t= 테스트 케이스 수
# k = 층 (1<k)
# n = 호 (n<=14)
# k층 n호에는 아래(k-1)층의 1-n호까지 사람의 합 만큼 살고 있음
# 0층 1-n명 살고 있음 = 1,2,3,...,n명
# 1층 1,3,6,10,...
# 2층 1, 4, 10, 20, 35, 56,...

t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    members = [num for num in range(1, n+1)]
    for a in range(k):  # 1층~k층
        current_members = []
        for b in range(1, n+1):
            current_members.append(sum(members[:b]))
        members = current_members.copy()
    print(members[-1])

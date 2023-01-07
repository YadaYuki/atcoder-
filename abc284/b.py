T = int(input())
ans = list()
for i in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    cnt = 0
    for a in A:
        if a % 2 == 1:
            cnt += 1
    ans.append(cnt)

for a in ans:
    print(a)
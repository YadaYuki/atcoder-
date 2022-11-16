N = int(input())
a = list(map(int,input().split()))

ans = 0
cnt = 0
cnt2 = 0
for i,v in enumerate(a):
    if i == v - 1:
        cnt += 1
    elif a[v-1] == i + 1:
        cnt2 += 1

ans += cnt * (cnt - 1) // 2
ans += cnt2 // 2
print(ans)



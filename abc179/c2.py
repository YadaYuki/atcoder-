N = int(input())
ans = 0

for A in range(1,N):
    
    ans += N // A
    if N % A == 0:
        ans -= 1 # 割り切れる場合は,C=0となってしまうので一つ向こう。
        continue

print(ans)

N = int(input())
H = list(map(int,input().split()))
th = max(H)
ans = H.index(th)
print(ans + 1)

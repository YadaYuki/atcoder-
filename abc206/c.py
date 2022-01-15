from collections import defaultdict
# 
N = int(input())
A = list(map(int,input().split()))

A_dict = defaultdict(int) # Aの要素の中で同じ値の要素が2つ以上存在する要素のみ格納

for i in range(N):
    A_dict[A[i]] += 1

ans = N * (N-1) // 2

for key,value in A_dict.items():
    ans -= value * (value-1) // 2

print(ans)

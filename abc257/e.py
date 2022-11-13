N = int(input())
C = list(map(int,input().split()))
min_C = min(C)

digit = N // min_C

ans = []

for d in  range(digit,0,-1):
    for i in range(8,-1,-1):
        c = C[i]
        rest_N = N - c
        rest_d = d - 1
        if rest_N >= min_C * rest_d:
            N -= c
            ans.append(i+1)
            break

print("".join([f"{a}" for a in ans]))
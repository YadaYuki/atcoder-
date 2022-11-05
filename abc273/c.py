N = int(input())
P = list(map(int,input().split()))


last_down_idx = -1

for i in range(N-1):
    if P[i] > P[i+1]:
        last_down_idx = i

max_val = -1
for i in range(last_down_idx+1,N):
    if P[last_down_idx] > P[i]:
        max_val = max(max_val,P[i])

ans = P[:last_down_idx]

max_idx = P.index(max_val)


P[last_down_idx],P[max_idx] = P[max_idx],P[last_down_idx]

ans.append(max_val)

s = P[last_down_idx+1:]

s = sorted(s,reverse=True)

ans.extend(s)

print(*ans)


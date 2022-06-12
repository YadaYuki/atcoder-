N = int(input())
A = list(map(int, input().split()))
A_sum = [0]

for i in A:
    if not i:
        A_sum.append(A_sum[-1] - 1)
    else:
        A_sum.append(A_sum[-1] + 1)

max_score = float('-inf')
min_val_for_i = 0 # i番目までの要素の中での最小値
min_score = float("inf")
max_val_for_i = 0 # i番目までの要素の中での最大値

for i in range(0,N+1):
    
    max_score = max(A_sum[i]-min_val_for_i,max_score)
    min_val_for_i = min(min_val_for_i,A_sum[i])

    min_score = min(A_sum[i]-max_val_for_i,min_score)
    max_val_for_i = max(max_val_for_i,A_sum[i])

print(max_score - min_score + 1)
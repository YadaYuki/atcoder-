
A = list(map(int,input().split()))
for i in range(N):
    weight = A[i]
    if A[i] <= W:
        good_choice_dict[weight] = 1
# 2個の選び方
for i in range(N-1):
    for j in range(i+1,N):
        weight = A[i] + A[j]
        if weight <= W:
            good_choice_dict[weight] = 1

# 3個の選び方
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            weight = A[i] + A[j] + A[k]
            if weight <= W:
                good_choice_dict[weight] = 1
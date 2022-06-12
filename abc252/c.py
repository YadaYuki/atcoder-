N = int(input())

S = []
for i in range(N):
    s = list(input())
    S.append(list(map(int,s)))

BIG = 10 ** 6
ans = BIG

def calulate_time(num:int):
    index_arr = []
    for i in range(N):
        index_arr.append(S[i].index(num))
    index_arr.sort()
    times_to_push = [-1] * N
    times_to_push[0] = index_arr[0]
    for i in range(1,N):
        if index_arr[i] == index_arr[i-1]:
            times_to_push[i] = times_to_push[i-1] + 10
        else:
            times_to_push[i] = index_arr[i]
    return max(times_to_push)
for num in range(0,10):
    ans = min(ans,calulate_time(num))

print(ans)



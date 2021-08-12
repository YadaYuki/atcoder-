N =int(input())
arr = list(map(int,input().split()))
ans_arr = [-1 for i in range(N)]

for i,item in enumerate(arr):
    ans_arr[item-1] = i + 1

for i in range(N):
    if i == N-1:
        print(ans_arr[i])
        break
    print(ans_arr[i],end=" ")
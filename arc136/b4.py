N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A_val = [0] * 5001
B_val = [0] * 5001

for i in range(N):
    A_val[A[i]] += 1
    B_val[B[i]] += 1


for i in range(5001):
    if A_val[i] != B_val[i]:
        print('No')
        exit()

for i in range(N):
    if A_val[A[i]] > 1:
        print('Yes')
        exit()


def bubble_sort(arr):
    for _ in range(N-2):
        for i in range(len(arr)-1,1,-1):
            minimum = min(arr[i-2], arr[i-1], arr[i])
            while arr[i-2] != minimum:
                arr[i-2], arr[i-1], arr[i] = arr[i], arr[i-2], arr[i-1]
            if arr[i] == minimum:
                arr[i-2], arr[i-1], arr[i] = arr[i], arr[i-2], arr[i-1]
    return arr


A = bubble_sort(A)
B = bubble_sort(B)

for i in range(N):
    if A[i] != B[i]:
        print('No')
        exit()


print('Yes')

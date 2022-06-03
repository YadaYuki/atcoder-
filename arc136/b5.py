
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-2):
            x,y,z = arr[j], arr[j+1], arr[j+2]
            minimum = min(x,y,z)
            while not arr[j] == minimum:
                x,y,z = arr[j], arr[j+1], arr[j+2]
                arr[j], arr[j+1], arr[j+2] = z, x, y
    return arr

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_sorted = sorted(A)
B_sorted = sorted(B)
d = {}
has_same = False

for i in range(N):
    if A_sorted[i] in d:
        has_same = True
    if A_sorted[i] != B_sorted[i]:
        print("No")
        exit()
    d[A_sorted[i]] = True


if has_same:
    print("Yes")
    exit()


A_sorted = bubble_sort(A)
B_sorted = bubble_sort(B)

for i in range(N):
    if A_sorted[i] != B_sorted[i]:
        print("No")
        exit()

print("Yes")

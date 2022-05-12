from collections import defaultdict
def original_bubble_sort(arr):
    completed = False
    while not completed:
        completed = True
        for i in range(len(arr) - 2):
            minimum = min(arr[i], arr[i+1], arr[i+2])
            if minimum != arr[i]:
                completed = False
            while arr[i] != minimum:
                arr[i], arr[i+1], arr[i+2] = arr[i+2], arr[i], arr[i+1]

    

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A_dict = defaultdict(int)
B_dict = defaultdict(int)

for i in range(N):
    A_dict[A[i]] += 1
    B_dict[B[i]] += 1
dup= True
for key in A_dict:
    if A_dict[key] != B_dict[key]:
        print('No')
        exit()
    if A_dict[key] > 1:
        dup = True

if not dup:
    print('Yes')
    exit()

original_bubble_sort(A)
original_bubble_sort(B)


for i in range(N):
    if A[i] != B[i]:
        print('No')
        exit()

print('Yes')

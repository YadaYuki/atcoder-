N = int(input())
A = list(map(int, input().split()))

if A[0] == 1 or (A[0] == 0 and A[1] == 0):
    print("No")
else:
    print("Yes")
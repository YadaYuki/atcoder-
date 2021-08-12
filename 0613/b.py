N = int(input())
A = [int(item) for item in input().split()]
is_exist_arr = [0 for _ in range(N)]

for i in range(N):
  is_exist_arr[A[i]-1] = 1

print("No" if (0 in is_exist_arr) else "Yes")



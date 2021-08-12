N = int(input())
C = list(map(int,input().split()))
ans = 1
C.sort()
divide_num = 10 ** 9 + 7

for i in range(N):
  ans = ans * max(0, C[i] - i) % 1000000007
print(ans % divide_num)




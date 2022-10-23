N,x,y = map(int,input().split())
A = list(map(int,input().split()))
A_odd = [A[i] for i in range(N) if i%2==0] # 0からxを作る
A_even = [A[i] for i in range(N) if i%2==1] # 0からyを作る

def coordinate_to_dpidx(c:int):
  return c + 10000

x_dp = [[False for _ in range(20001)] for _ in range(len(A_odd)+1)]
y_dp = [[False for _ in range(20001)] for _ in range(len(A_even)+1)]

x_dp[0][coordinate_to_dpidx(0)] = True
x_dp[1][coordinate_to_dpidx(A_odd[0])] = True
y_dp[0][coordinate_to_dpidx(0)] = True


# x_dp
for i in range(2,len(A_odd)+1):
  for x_idx in range(-10000,10001):
    if x_idx-A_odd[i-1] >= -10000:  
      x_dp[i][coordinate_to_dpidx(x_idx)] = x_dp[i-1][coordinate_to_dpidx(x_idx-A_odd[i-1])] or x_dp[i][coordinate_to_dpidx(x_idx)]
    if x_idx+A_odd[i-1] <= 10000:
      x_dp[i][coordinate_to_dpidx(x_idx)] = x_dp[i-1][coordinate_to_dpidx(x_idx+A_odd[i-1])] or x_dp[i][coordinate_to_dpidx(x_idx)]

# print([[i-10000 for i, x in enumerate(x_dp[j]) if x == True] for j in range(len(x_dp))])
# y_dp
for i in range(1,len(A_even)+1):
  for y_idx in range(-10000,10000+1):
    if y_idx-A_even[i-1] >= -10000:  
      y_dp[i][coordinate_to_dpidx(y_idx)] = y_dp[i-1][coordinate_to_dpidx(y_idx-A_even[i-1])] or y_dp[i][coordinate_to_dpidx(y_idx)]
    if y_idx+A_even[i-1] <= 10000:
      y_dp[i][coordinate_to_dpidx(y_idx)] = y_dp[i-1][coordinate_to_dpidx(y_idx+A_even[i-1])] or y_dp[i][coordinate_to_dpidx(y_idx)]

# print([[i-10000 for i, x in enumerate(x_dp[j]) if x == True] for j in range(len(x_dp))])
if x_dp[len(x_dp)-1][coordinate_to_dpidx(x)] and y_dp[len(y_dp)-1][coordinate_to_dpidx(y)]:
    print("Yes")
else:
    print("No")




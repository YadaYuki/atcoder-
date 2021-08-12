N,D,H = [int(item) for item in input().split()]

ans = 0

def get_height_up_stairs(h,d,D,H):
  return (h*D - d*H)/(D-d)

for i in range(N):
  d,h = [int(item) for item in input().split()]
  ans = max(ans,get_height_up_stairs(h, d, D, H))

print(ans)

N,K = [int(item) for item in input().split()]

point_arr = []

for i in range(N):
  point_arr.append([int(item) for item in input().split()])

current_loc = 0

ans = 0

point_arr = sorted(point_arr, key=lambda k: k[0]) 

for i in range(N):
  distance_to_next_point = point_arr[i][0] - current_loc # A
  if distance_to_next_point > K:
    break
  else:
    K = K  + point_arr[i][1]
ans += K
print(ans)

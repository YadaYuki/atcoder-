N = int(input())
coordinate_arr = []
coordinate_map = {}
for _ in range(N):
  x,y = map(int,input().split())
  coordinate_arr.append([x,y])
  coordinate_map[",".join([str(x),str(y)])] = True


count = 0

for i in range(N-1):
  for j in range(i+1,N):
    right_up,left_down = coordinate_arr[i],coordinate_arr[j]
    if right_up[0] == left_down[0] or right_up[1] == left_down[1]: # x座標が同じであった場合、長方形にはならない。
      continue
    else:
      right_down = [right_up[0],left_down[1]]
      left_up = [left_down[0],right_up[1]]
      # right_downとleft_upの両方が存在した場合、長方形が成立
      if coordinate_map.get(",".join(map(str,right_down))) and coordinate_map.get(",".join(map(str,left_up))):
        count += 1

print(int(count/2))




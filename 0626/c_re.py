N = int(input())
segment_arr = []

def convert_segment(t,l,r):
  if t == 1:
    return [l,r]
  elif t == 2:
    return [l,r-0.5]
  elif t == 3:
    return [l+0.5,r]
  elif t == 4:
    return [l+0.5,r-0.5]

def is_overlap(s1,s2):
  return max(s1[0],s2[0]) <= min(s1[1],s2[1])

for _ in range(N):
  t,l,r = map(int,input().split())
  segment_arr.append(convert_segment(t,l,r))

ans = 0

for i in range(N-1):
  for j in range(i+1,N):
    ans += int(is_overlap(segment_arr[i],segment_arr[j]))

print(ans)


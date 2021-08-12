N = int(input())

def adjust_to_closed_section(t,section):
  adjusted_section = section
  if t == 1:
    pass
  elif t == 2:
    adjusted_section[1] = section[1] - 0.5
  elif t == 3:
    adjusted_section[0] = section[0] + 0.5
  elif t == 4:
    adjusted_section[0] = section[0] + 0.5
    adjusted_section[1] = section[1] - 0.5
  return adjusted_section

def has_common_section(closed_section_1,closed_section_2):
  return max(closed_section_1[0],closed_section_2[0]) <= min(closed_section_1[1],closed_section_2[1])

closed_section_arr = []
for i in range(N):
  t,l,n = [int(item) for item in input().split()]
  section = [l,n]
  closed_section_arr.append(adjust_to_closed_section(t,section))

ans = 0

for i in range(N-1):
  for j in range(i+1,N):
    ans += int(has_common_section(closed_section_arr[i],closed_section_arr[j]))

print(ans)

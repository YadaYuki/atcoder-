

from itertools import combinations

def get_team_power(members):
  power = float("inf")
  for i in range(5):
    val = 0
    for j in range(3):
      val = max(val,members[j][i])
    power = min(val,power)
  return power

N = int(input())
member_data = []
for i in range(N):
  member = [int(item) for item in input().split()]
  member_data.append(member)

combs = list(combinations(member_data, 3))

max_power = 0

for i in range(len(combs)):
  max_power = max(max_power,get_team_power(combs[i]))

print(max_power)


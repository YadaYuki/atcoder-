import sys
sys.setrecursionlimit(1000000)

N = int(input())

child = [[] for _ in range(N)]

for i in range(N-1):
  B = int(input())
  child[B-1].append(i+1)


def dfs(person):
  if len(child[person]) == 0:
    return 1
  else:
    child_salary = []
    for i in range(len(child[person])):
      child_salary.append(dfs(child[person][i]))
    return max(child_salary) + min(child_salary) + 1


print(dfs(0))


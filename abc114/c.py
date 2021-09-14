N = int(input())


ans = 0
def dfs(val:int):
  global ans

  if val > N:
    return
  if "3" in str(val) and "5" in str(val) and "7" in str(val):
    ans += 1
  
  dfs(val * 10 + 3)
  dfs(val * 10 + 5)
  dfs(val * 10 + 7)

dfs(0)

print(ans)


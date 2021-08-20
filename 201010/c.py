


if __name__ == "__main__":
  N = int(input())
  p = list(map(int, input().split()))
  hash = {}
  min_val = 0
  for i in range(N):
    if min_val == p[i]:
      min_val += 1
      while hash.get(min_val) == True:
        min_val += 1
    print(min_val)
    hash[p[i]] = True
    






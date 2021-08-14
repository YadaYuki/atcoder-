N,K = map(int,input().split())
c = list(map(int,input().split()))

hash = {} # 区間Kにおける要素とその数を保存

# hashの初期化
for i in range(K): 
  if hash.get(c[i]) == None:
    hash[c[i]] = 1
  else:
    hash[c[i]] += 1

ans = len(hash)

for i in range(1,N-K+1):
  # decrement prefix
  candy_deleted = c[i-1]
  if hash[candy_deleted] == 1:
    hash.pop(candy_deleted)
  else:
    hash[candy_deleted] -= 1
  # suffix
  suffix_pushed = c[i+K-1]
  if hash.get(suffix_pushed) == None:
    hash[suffix_pushed] = 1
  else:
    hash[suffix_pushed] += 1
  ans = max(ans,len(hash))

print(ans)


N = int(input())
a = []

for i in range(N-1):
  a.append( [0] * (i+1)+ list(map(int,input().split())))

def to_binary(n,length):
  return list(bin(n)[2:].zfill(length))

# 全ての組み合わせに対して、幸福度の総和を計算

happy = []

for i in range(2**N):
  binary = to_binary(i,N)
  happy_sum = 0
  for j in range(0,N):
    for k in range(j+1,N):
      if binary[j] == "1" and binary[k] == "1":
        happy_sum += a[j][k] # j < k
  happy.append(happy_sum)

# グループ分け


ans = -1
for n1 in range(2**N):
  for n2 in range(2**N):
    if n1 & n2 > 0:
      continue
    n3 = 2 ** N - 1 - (n1 | n2)
    ans = max(ans,happy[n1] + happy[n2] + happy[n3])

print(ans)

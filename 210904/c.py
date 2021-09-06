N = int(input())
p = list(map(int,input().split()))
q_dict = {}
for i in range(N):
  q_dict[p[i]] = i + 1

ans = ""
for i in range(N):
  ans += "{} ".format(q_dict[i+1])

print(ans)

p = list(map(int,input().split()))

ans = ""
a = "a"

for i in range(26):
  ans += chr(ord(a) + p[i] - 1)

print(ans)

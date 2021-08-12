num = 1234567890
ans = 0

for i in range(1,5000000):
  if num % i == 0:
    ans += i

print(ans)

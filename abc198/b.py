N = input()

if N == "0":
  print("Yes")
  exit(0)

def is_palindrome(s:str):
  N = len(s)
  half_N = int(N/2)
  for i in range(half_N):
    if s[(N-1)-i] != s[i]:
      return False
  return True

zero_count = 0

i = len(N) - 1

while N[i] == '0':
  zero_count += 1
  i -= 1

if is_palindrome("0" * zero_count + N):
  print("Yes")
else:
  print("No")







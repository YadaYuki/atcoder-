A, B, C = [int(item) for item in input().split()]


def is_negative(n):
  return n < 0

if A == B:
  print("=")
  exit(0)

if C % 2 == 0:
  if abs(A) == abs(B):
    print("=")
  elif abs(A) > abs(B):
    print(">")
  else:
    print("<")
  exit(0)
    

if is_negative(A) == True:
  if is_negative(B) == True:
    if A < B:
      print("<")
    else:
      print(">")
  else:
    print("<")
else:
  if is_negative(B) == True:
    print(">")
  else:
    if A > B:
      print(">")
    else:
      print("<")

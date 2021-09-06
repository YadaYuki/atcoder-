N = int(input())

ans,current_value = "",N

while current_value != 0:
  if current_value % 2 == 1:
    ans = "A" + ans
    current_value -= 1
  else:
    ans = "B" + ans
    current_value /= 2

print(ans)
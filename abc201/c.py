S = input()

necessary_num = [i for i in range(10) if S[i] == "o"]
invalid_num = [i for i in range(10) if S[i] == "x"]

def is_valid(num:int):
  num_str = str(num).zfill(4)
  for item in necessary_num:
    if not (str(item) in num_str):
      return False
  for item in invalid_num:
    if str(item) in num_str:
      return False
  return True


ans = 0

for i in range(10000):
  ans += int(is_valid(i))

print(ans)
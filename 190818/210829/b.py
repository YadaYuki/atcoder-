N = int(input())

dict = {}
is_exist=False
for i in range(N):
    s, t = input().split()
    if dict.get(s) == None:
        dict[s] = {t: True}
    else:
      first_name_dict = dict[s]
      if first_name_dict.get(t) == None:
        first_name_dict[t] = True
      else:
        is_exist = True

print("Yes" if is_exist == True else "No")

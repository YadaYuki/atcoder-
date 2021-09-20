from functools import cmp_to_key
new_alphabet = input()

new_alphabet_idx_map = {}

for i in range(26):
  new_alphabet_idx_map[new_alphabet[i]] = i # 新アルファベットにおいて何番目か？

def sort_by(a:str,b:str):
  length_a = len(a)
  length_b = len(b)
  for i in range(min(length_a,length_b)):
    if new_alphabet_idx_map[a[i]] > new_alphabet_idx_map[b[i]]: # aの方が辞書順で後に登場
      return 1
    elif new_alphabet_idx_map[a[i]] < new_alphabet_idx_map[b[i]]:
      return -1
    elif new_alphabet_idx_map[a[i]] == new_alphabet_idx_map[b[i]]:
      continue
  return length_a - length_b

N = int(input())
S = []
for i in range(N):
  S.append(input())

ans = sorted(S, key=cmp_to_key(sort_by))

for i in range(N):
  print(ans[i])

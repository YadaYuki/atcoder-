import itertools

S,K = input().split()
K = int(K)
N = len(S)
S = sorted(S)


K_idx_arr = list(itertools.permutations([i for i in range(N)]))
dict = {}
dict_arr = []

for i in range(len(K_idx_arr)):
  idx_arr = K_idx_arr[i]
  s = ""
  for j in range(N):
    s += S[idx_arr[j]]
  if dict.get(s) == None:
    dict_arr.append(s)
    dict[s] = True

print(dict_arr[K-1])









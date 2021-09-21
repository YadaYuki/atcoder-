import sys
sys.setrecursionlimit(1000000)

N = int(input())
subordinate_arr=[[] for _ in range(N)] # iが持つ部下を保存する配列
for i in range(N-1):
  B = int(input())
  subordinate_arr[B-1].append(i+1)


# 再帰により、給与を求める
def get_sarary(person:int):
  if len(subordinate_arr[person]) == 0:
    return 1
  else:
    min_sarary_of_subordinate = float("inf")
    max_sarary_of_subordinate = -1
    for subordinate in subordinate_arr[person]:
      sarary = get_sarary(subordinate)
      min_sarary_of_subordinate = min(sarary,min_sarary_of_subordinate)
      max_sarary_of_subordinate = max(sarary,max_sarary_of_subordinate)
    return min_sarary_of_subordinate + max_sarary_of_subordinate + 1


print(get_sarary(0))







if __name__ == "__main__":
  H,W,N = map(int,input().split())
  number_coordinate_arr = []
  A_arr,B_arr = [],[]
  for i in range(N):
    A,B = map(int,input().split())
    A_arr.append(A)
    B_arr.append(B)
  sorted_A = sorted(A_arr)
  sorted_B = sorted(B_arr)
  A_idx_map,B_idx_map = {},{}

  for i in range(N):
    if A_idx_map.get(sorted_A[i]) == None:
      A_idx_map[sorted_A[i]] = i + 1
    if B_idx_map.get(sorted_B[i]) == None:
      B_idx_map[sorted_B[i]] = i + 1

  for i in range(N):
    A,B = A_arr[i],B_arr[i]
    print("{} {}".format(A_idx_map[A],B_idx_map[B]))
  


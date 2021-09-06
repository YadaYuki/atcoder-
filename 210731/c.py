if __name__ == "__main__":
  N,M = map(int,input().split())
  A = list(map(int,input().split()))
  B = list(map(int,input().split()))

  A.sort()
  B.sort()
  i,j = 0,0
  ans = float("inf")
  while j < M and i < N:
    if j == M-1:
      break
    if abs(A[i]-B[j]) < abs(A[i]-B[j+1]):
      ans = min(ans,abs(A[i]-B[j]))
      i += 1
    else:
      j += 1
  
  if j != M:
    while j < M :
      ans = min(ans,abs(A[N-1]-B[j]))
      j += 1
  if i != N:
    while i < N :
      ans = min(ans,abs(A[i]-B[M-1]))
      i += 1

  print(ans)
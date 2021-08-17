
def main(N,M,A,B):
  ans = float("inf")
  A.sort()
  B.sort()
  j = 0
  for i in range(N):
    while True:
      ans = min(abs(A[i]-B[j]),ans)
      if j == N-1:
        break
      if abs(A[i] - B[j]) < abs(A[i] - B[j+1]):
        break
      j += 1
  print(ans)    

def main_ans(N,M,A,B):
  A.sort()
  B.sort()
  i,j = 0,0
  ans = float("inf")
  while i < N and j < M:
    ans = min(abs(A[i] - B[j]),ans)
    if A[i] > B[j]:
      j += 1
    else:
      i += 1
    
  print(ans)


if __name__=='__main__':
  N,M = map(int,input().split())
  A = list(map(int,input().split()))
  B = list(map(int,input().split()))
  main_ans(N,M,A,B)
  # main(3,3,[1,3,5],[100,500,1000])
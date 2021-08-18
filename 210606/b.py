
def main(N,A):
  nuts = 0
  for i in range(N):
    nuts += max(0,A[i]-10)
  print(nuts)


if __name__=='__main__':
  N = int(input())
  A = list(map(int,input().split()))
  main(N,A)

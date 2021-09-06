if __name__ == "__main__":
  N = int(input())
  S = list(map(int,input().split()))
  T = list(map(int,input().split()))
  t = [0] * N
  t[0] = T[0]
  for i in range(1,N):
    t[i] = min(t[i-1] + S[i-1],T[i])
  if t[0] > t[N-1] + S[N-1]:
    t[0] = t[N-1] + S[N-1]
    for i in range(1,N):
      t[i] = min(t[i-1] + S[i-1],T[i])
  

  for i in range(N):
    print(t[i])
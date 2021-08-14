def main(N,S,T):
  time_first_get = [0] * N  # 1くんがもらう時間をt1で固定

  time_first_get[0] = T[0]

  for i in range(1, N):
      time_first_get[i] = min(T[i], time_first_get[i-1] + S[i-1])

  if time_first_get[0] > time_first_get[N-1] + S[N-1]:
    time_first_get[0] = time_first_get[N-1] + S[N-1]
    for i in range(1, N):
      time_first_get[i] = min(T[i], time_first_get[i-1] + S[i-1])
  
  for i in range(N):
      print(time_first_get[i])
  

if __name__ == "__main__":
  N = int(input())
  S = list(map(int, input().split()))
  T = list(map(int, input().split()))
  main(N,S,T)


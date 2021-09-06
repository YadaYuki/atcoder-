def is_prime(n):
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      return False
  return True

def get_prime_decomposition(n):
    prime_decomposition = []
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            prime_decomposition.append(i)
            n = int(n/i)
    if n != 1:
      prime_decomposition.append(n)
    return prime_decomposition


N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [True for _ in range(0,M)]

for i in range(N):
  prime_set = set(get_prime_decomposition(A[i]))
  for prime in prime_set:
    if prime > M:
      break
    if S[prime - 1] == False:
      continue
    i = prime
    while  i <= M:
      S[i-1] = False
      i += prime
  
print(sum(S))
for i in range(M):
  if S[i] == True:
    print(i+1)

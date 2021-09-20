N = int(input())
mountains = []
for _ in range(N):
  S,T = input().split()
  mountains.append((S,int(T)))

print(sorted(mountains,key=lambda mountain:mountain[1])[-2][0])

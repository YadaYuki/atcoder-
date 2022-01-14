N,X = map(int,input().split())
A = list(map(int,input().split()))

know = [False for _ in range(N)]

i = X - 1

while know[i] != True:
    know[i] = True
    i = A[i] - 1 # A[i]くんに秘密をばらす

print(sum(know))
    

N = int(input())
A = [list(input()) for _ in range(N)]

def inverse(k):
    d = {
        "W":"L","L":"W","D":"D"
    }
    return d[k]

for i in range(N-1):
    for j in range(i+1,N):
        if inverse(A[i][j]) != A[j][i]:
            print("incorrect")
            exit()

print("correct")
import sys
sys.setrecursionlimit(2*10**5+1)

parents = [-1] * 2 * 10**5

def union(x,y):
    x,y = find(x), find(y)
    if x == y:
        return
    parents[y] = x


def find(x):
    if parents[x] < 0:
        return x
    parents[x] = find(parents[x])
    return parents[x]

N = int(input())
A = list(map(int, input().split()))

unique_A = set(A)

num_of_graph = 0

num_of_elem = [0] * (2 * 10**5)

for i in range(N//2):
    if A[i] != A[N-i-1]:
        union(A[i]-1, A[N-1-i]-1)


for i in range(2 * 10**5):
    num_of_elem[find(i)] += 1

ans = 0
for i in range(2*10**5):
    if num_of_elem[i] > 1:
        ans += num_of_elem[i] - 1

print(ans)







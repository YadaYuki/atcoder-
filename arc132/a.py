n = int(input())
R = list(map(int, input().split()))
C = list(map(int, input().split()))

q = int(input())
query = []

for _ in range(q):
    r,c = map(int, input().split())
    query.append([r-1,c-1])

def is_painted(r,c) -> bool:
    painted_trout_r = R[r]
    painted_trout_c = C[c]
    if painted_trout_r + painted_trout_c > n:
        return True
    return False

ans = []
for q in query:
    r,c = q
    if is_painted(r,c):
        ans.append('#')
    else:
        ans.append('.')

print(''.join(ans))










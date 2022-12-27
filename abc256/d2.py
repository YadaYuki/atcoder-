N,P,Q,R = map(int,input().split())
A = list(map(int,input().split()))

s = 0
r = 0
x_map = {}
for l in range(N):
    while r < N and s < P:
        s += A[r]
        r += 1
    if s == P:
        x_map[l] = r - 1
    s -= A[l]

s = 0
r = 0
y_map = {}
for l in range(N):
    while r < N and s < Q:
        s += A[r]
        r += 1
    if s == Q:
        y_map[l] = r - 1
    s -= A[l]
s = 0
r = 0
z_map = {}
for l in range(N):
    while r < N and s < R:
        s += A[r]
        r += 1
    if s == R:
        z_map[l] = r - 1
    s -= A[l]

for x_s,x_e in x_map.items():
    if (x_e + 1) in y_map:
        y_s = x_e + 1
        y_e = y_map[y_s]
        if (y_e + 1) in z_map:
            print("Yes")
            exit()
print("No")
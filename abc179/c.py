N = int(input())

b_count = 0

for A in range(1,N):
    b_count += (N-1)// A

print(b_count)



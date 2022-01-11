import math
N = int(input())

ans = 0

for A in range(1,math.floor(N ** (1/3)) + 1):
    for B in range(A,math.floor((N/A)**(1/2))+1):
        ans += math.floor(N/(A*B)) + 1 - B

print(ans)
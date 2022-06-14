import math

def calc_sum(n,a,d):
    return n * (2*a + (n-1)*d) // 2

N,A,B = map(int,input().split())

n_A = N // A
n_B = N // B
ans = calc_sum(N,1,1)
ans -= calc_sum(n_A,A,A)
ans -= calc_sum(n_B,B,B)

lcm = A * B // math.gcd(A,B)

n_lcm = N // lcm

ans += calc_sum(n_lcm,lcm,lcm)

print(ans)


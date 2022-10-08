
def gcd(a,b):
    return a if b == 0 else gcd(b, a % b)

def lcm(a,b):
    return a * b // gcd(a,b)

N,A,B = map(int,input().split())
x_all = N * (1+N) // 2

n_A = N // A
l_A = n_A * A
x_A = n_A * (A + l_A) // 2

n_B = N // B
l_B = n_B * B
x_B = n_B * (B + l_B) // 2

lcm_AB = lcm(A,B)

n_lcm_AB = N // lcm_AB
l_lcm_AB = n_lcm_AB * lcm_AB
x_lcm_AB = n_lcm_AB * (lcm_AB + l_lcm_AB) // 2

print(x_all - x_A - x_B + x_lcm_AB)
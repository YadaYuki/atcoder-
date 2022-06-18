MOD = 998244353

N = int(input())
N_sqrt = int(N ** 0.5)
ans = 0
for q in range(1,N_sqrt+1):
    p_min = q
    p_max = N // q
    p_num = (p_max - p_min + 1) // 2
    q_mod = q % 2
    if p_min % 2 == q_mod and p_max % 2 == q_mod:
        p_num += 1

    ans += p_num % MOD
    ans %= MOD
print(ans)

def trial_division(n: int):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1: a.append(n)
    # Only odd number is possible
    return a

        
prime_list_for_A = set()

N,M = map(int,input().split())
A = list(map(int,input().split()))


max_A=max(A)
already_checked_prime = [False] * (max_A+1)
is_ans = [True] * (M+1)
for i in range(N):
    if A[i] > 1:
        prime_factorization_set =  set(trial_division(A[i]))
        for prime in prime_factorization_set:
            if not already_checked_prime[prime]:
                for i in range(prime,M+1,prime):
                    is_ans[i] = False
                already_checked_prime[prime] = True

ans = [i for i in range(1,M+1) if is_ans[i]]

print(len(ans))
for i in range(len(ans)):
    print(ans[i])
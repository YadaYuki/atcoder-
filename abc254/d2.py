from collections import defaultdict

def is_square(n:int):
    return n == int(n**0.5) ** 2

def list_divisors(n:int):
    n_square = int(n ** 0.5)
    divisors = set()
    for divisor_candidate in range(1,n_square+1):
        if n % divisor_candidate == 0:
            divisors.add(divisor_candidate)
            divisors.add(n//divisor_candidate)

    return list(divisors)

N = int(input())
nfn_map = defaultdict(int)
for i in range(1,N+1):
    divisors = list_divisors(i)
    fn = -1
    for divisor in divisors:
        if is_square(divisor):
            fn = max(fn,divisor)
    
    nfn_map[i//fn] += 1


ans = 0

for k,v in nfn_map.items():
    ans += v * (v-1)
ans += N
print(ans)

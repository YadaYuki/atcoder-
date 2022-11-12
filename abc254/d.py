
from collections import defaultdict
def f(x:int):
    f_val = -1
    for i in range(1,int(x ** 0.5)+1):
        if x % i == 0:
            sqrt_i = int(i**0.5)
            i_is_square = (i == sqrt_i ** 2)
            if i_is_square:
                f_val = max(i,f_val)
            i_pair = x//i
            sqrt_i_pair = int((i_pair)**0.5)
            i_pair_is_square = (i_pair == sqrt_i_pair ** 2)
            if i_pair_is_square:
                f_val = max(i_pair,f_val)
    return f_val

f_to_cnt = defaultdict(int)

N = int(input())

for i in range(1,N+1):
    f_to_cnt[i//f(i)] += 1

ans = 0

for k,v in f_to_cnt.items():
    ans += v * (v-1)

print(ans + N)
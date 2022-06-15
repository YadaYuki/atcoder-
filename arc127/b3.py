from copy import copy
N,L = map(int,input().split())

def convert_int_to_tertiary_str(n:int):
    ls = []
    while n > 0:
        ls.append(n%3)
        n //= 3
    ls.reverse()
    return ls


BASE = 2 * (3**(L-1))

ans = []
for i in range(N):
    ans.append(convert_int_to_tertiary_str(BASE + i))

for d in [1,2]:
    for i in range(N):
        digits = []
        for bit in ans[i]:
            digits.append((bit+d)%3)
        ans.append(digits)
    
    



for i in ans:
    print("".join(map(str,i)))
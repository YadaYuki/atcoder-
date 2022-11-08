N = int(input())
a = list(map(int,input().split()))

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while n % 3 == 0:
        if n % f == 0:
            a.append(f)
            n //= f
    if n != 1:
        a.append(n)
    return a

min_two = 10**9
min_three = 10**9
two_and_three_cnts = []
s = set()
for i in range(N):
    v = a[i]
    two_and_three_cnt = {2:0,3:0}
    if v != 1:
        pf = prime_factorize(v)
        for p in pf:
            if p == 2:
                two_and_three_cnt[2] += 1
            elif p== 3:
                two_and_three_cnt[3] += 1
            else:
                if i == 0:
                    s.add(p)
                else:
                    if p not in s:
                        print(-1)
                        exit()
    min_two = min(min_two,two_and_three_cnt[2])
    min_three = min(min_three,two_and_three_cnt[3])
    two_and_three_cnts.append(two_and_three_cnt)

ans = 0
for item in two_and_three_cnts:
    two = item[2]
    three = item[3]
    ans += two - min_two
    ans += three - min_three

print(ans)

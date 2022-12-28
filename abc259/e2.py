N = int(input())
a = list()

p_2_e = {} # {"[素数p]": [指数e,素数p^eの登場回数]}

for i in range(N):
    pe = list()
    m = int(input())
    for j in range(m):
        p,e = map(int,input().split())
        pe.append([p,e])

        if p not in p_2_e:
            p_2_e[p] = [e,1]
        else:
            if p_2_e[p][0] < e:
                p_2_e[p] = [e,1]
            elif p_2_e[p][0] == e:
                p_2_e[p][1] += 1
    a.append(pe)
ans = 0
for i in range(N):
    pe = a[i]
    for p,e in pe:
        if p_2_e[p][0] == e and p_2_e[p][1] == 1:
            ans += 1
            break

if ans < N:
    ans += 1

print(ans)


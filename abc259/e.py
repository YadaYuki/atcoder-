N = int(input())
a = []
for i in range(N):
    m = int(input())
    l = []
    for j in range(m):
        p,e = map(int,input().split())
        l.append([p,e])
    a.append(l)

LCM = {
#  "素数": {"添字","登場回数"}
}
for i in range(N):
    l = a[i]
    for j in range(len(l)):
        p,e = l[j]
        if p in LCM:
            if LCM[p][0] == e:
                LCM[p][1] += 1
            elif LCM[p][0] < e:
                LCM[p] = [e,1]
        else:
            LCM[p] = [e,1]
                
ans = 0
for i in range(N):
    ai = a[i]
    change_lcm = False
    for j,pe in enumerate(ai):
        p,e = pe
        if LCM[p][0] == e and LCM[p][1] == 1:
            change_lcm = True
            break
    ans += int(change_lcm)
if N == ans:
    print(ans)
else:
    print(ans + 1)
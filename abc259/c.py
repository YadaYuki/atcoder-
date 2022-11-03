from collections import OrderedDict


S = list(input())
T = list(input())
N = len(S)

ds = [[S[0],1]]

for i in range(1,len(S)):
    if S[i] == S[i-1]:
        ds[-1][1] += 1
    else:
        ds.append([S[i],1])
dt = [[T[0],1]]
for i in range(1,len(T)):
    if T[i] == T[i-1]:
        dt[-1][1] += 1
    else:
        dt.append([T[i],1])


if len(ds) != len(dt):
    print("No")
    exit()

for i in range(len(ds)):
    s,t = ds[i],dt[i]
    if s[0] != t[0]:
        print("No")
        exit()
    else:
        if s[1] == t[1]:
            continue
        if s[1] > t[1]:
            print("No")
            exit()
        if s[1] == 1:
            print("No")
            exit()


print("Yes")
    


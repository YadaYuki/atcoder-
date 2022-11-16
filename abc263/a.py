from collections import defaultdict
a,b,c,d,e = list(map(int,input().split()))

dic = defaultdict(int)
for i in [a,b,c,d,e]:
    dic[i] += 1

if len(dic) == 2:
    for k,v in dic.items():
        if v == 2 or v == 3:
            print("Yes")
            exit()
print("No")
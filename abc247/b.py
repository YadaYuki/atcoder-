N = int(input())
st = [list(input().split()) for _ in range(N)]

for i in range(N):
    s,t = st[i]
    has_s, has_t = False, False
    for j in range(N):
        if i == j:
            continue
        else:
            sj,tj = st[j]
            if sj == s or tj == s:
                has_s = True # 他の人の姓名いずれかにsが含まれている
            if sj == t or tj == t: # 他の人の姓名いずれかにtが含まれている
                has_t = True
    if has_s and has_t:
        print('No')
        exit()

print("Yes")
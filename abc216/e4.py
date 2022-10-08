N,K  = map(int,input().split())
A = list(map(int,input().split()))

# mより大きいB[i]の数がK以下になるようなmの最小値
ok,ng = 2 * 10 ** 9 + 1,-1
while ok - ng > 1:
    mid = (ok + ng) // 2
    cnt = 0
    for a in A:
        b_num = max(0,a-mid)
        cnt += b_num
        # 2部探索の中にO(n)の計算が入るのめずらしい(はじめて)
    if cnt <= K:
        ok = mid
    else:
        ng = mid

ans = 0

for a in A:
    b_num = max(0,a-ok)
    ans += ((ok+1) + a) * b_num // 2
    K -= b_num

if K > 0:
    ans += K * ok

print(ans)
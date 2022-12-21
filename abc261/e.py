def k_th_bit(num:int,k:int):
    return num >> k & 1

N,C = map(int,input().split())
query = [list(map(int,input().split())) for _ in range(N)]
ans = [0] * N
for k in range(30):
    kth_bit_after_query = k_th_bit(C, k)
    func = [0,1]
    for i in range(N):
        t,a = query[i]
        kth_bit_in_A = k_th_bit(a, k)
        f = None
        if t == 1:
            f = [0 & kth_bit_in_A, 1 & kth_bit_in_A]
        if t == 2:
            f = [0 | kth_bit_in_A, 1 | kth_bit_in_A]
        if t == 3:
            f = [0 ^ kth_bit_in_A, 1 ^ kth_bit_in_A]
        func = [f[func[0]],f[func[1]]]
        kth_bit_after_query = func[kth_bit_after_query]
        # kth_bit_after_query: クエリi-1までを実行した後のk番目のビットが入る。なのでqueryiをこれに対して実行した場合、クエリiまで全てのクエリを計算を行ったビットが生成される
        ans[i] |= kth_bit_after_query << k # ans[i]のkビット目にクエリを入れる

for a in ans:
    print(a)
def kth_bit(num,k):
    return num >> k & 1

N,C = map(int,input().split())
query = [list(map(int,input().split())) for _ in range(N)]
ans = [0] * N
for k in range(30):
    k_th_bit_after_query = kth_bit(C, k)
    combined_func = [0,1]
    for i in range(N):
        t,a = query[i]
        k_th_bit_in_A = kth_bit(a, k)
        func = None
        if t == 1:
            func = [0 & k_th_bit_in_A, 1 & k_th_bit_in_A]
        if t == 2:
            func = [0 | k_th_bit_in_A, 1 | k_th_bit_in_A]
        if t == 3:
            func = [0 ^ k_th_bit_in_A, 1 ^ k_th_bit_in_A]
        combined_func = [func[combined_func[0]],func[combined_func[1]]] # fはなにで、なぜ更新しているんだ？というのが直感的に理解できない...。 これで
        # combined_func[0]には0に対してクエリiまでのcombined_funcを実行した結果が入っている
        k_th_bit_after_query = combined_func[k_th_bit_after_query]
        ans[i] |= k_th_bit_after_query << k

for a in ans:
    print(a)
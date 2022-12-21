N,C = map(int,input().split())

query = [list(map(int,input().split())) for i in range(N)]


def i_th_bit(x,i):
    return x >> i & 1

ans = [0] * N
for i in range(30):
    c_i_th_bit = i_th_bit(C, i)
    combined_func = [0,1] #
    for j,[T,A] in enumerate(query):
        A_i_th_bit = i_th_bit(A, i)
        if T == 1:
            combined_func = [combined_func[0] & A_i_th_bit,combined_func[1] & A_i_th_bit]
        if T == 2:
            combined_func = [combined_func[0] | A_i_th_bit,combined_func[1] | A_i_th_bit]
        if T == 3:
            combined_func = [combined_func[0] ^ A_i_th_bit,combined_func[1] ^ A_i_th_bit]
        c_i_th_bit = combined_func[c_i_th_bit]
        ans[j] = ans[j] + (c_i_th_bit << i)


for a in  ans:
    print(a)
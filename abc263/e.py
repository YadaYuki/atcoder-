N,C = map(int,input().split())

def kth_bit(n,k):
    return n >> k & 1
query = [list(map(int,input().split())) for _ in range(N)]
ans = [0 for i in range(N)]
for bit in range(30):
    combined_func = [0,1]
    x = kth_bit(C, bit)
    for j in range(N):
        t,a = query[j]
        a_bit = kth_bit(a, bit)
        func = None
        if t == 1:
            func = [0 & a_bit, 1 & a_bit]
        if t == 2:
            func = [0 | a_bit, 1 | a_bit]
        if t == 3:
            func = [0 ^ a_bit, 1 ^ a_bit]
        
        combined_func = [
            func[combined_func[0]],func[combined_func[1]]
        ]
        x = combined_func[x]
        ans[j] |= x << bit

for a in ans:
    print(a)




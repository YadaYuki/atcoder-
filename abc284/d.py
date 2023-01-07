# p * p * q なので p or qのいずれかは必ず 3 * (10 ^ 6) 以下になる

T = int(input())

pq_max = 3 * (10 ** 6)

for i in range(T):
    N = int(input())
    # check p
    for n in range(2,pq_max):
        if N % n == 0:
            if N % (n * n) == 0:
                p,q = n , N//(n*n)
                print(p,q)
            else:
                q,p = n,int((N//n)**0.5)
                print(p,q)
            break
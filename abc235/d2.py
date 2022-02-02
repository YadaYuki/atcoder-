from collections import deque

a,N = map(int, input().split())

queue = deque([1])


cost = { 1:0 }

d_N = len(str(N))

if N == 1:
    print(0)
    exit()

while len(queue) > 0:
    n = queue.popleft()
    cost_n = cost[n]
    if n % 10 != 0:
        dn = len(str(n))
        n_1 = n // 10
        n_2 = (n % 10) * (10 ** (len(str(n))-1))
        if n_1 + n_2 == N:
            print(cost_n + 1)
            exit()
        else:
            if n_1 + n_2 not in cost:
                cost[n_1 + n_2] = cost_n + 1
                queue.append(n_1 + n_2)
        
    if len(str(n * a)) <= d_N:
        if n * a == N:
            print(cost_n + 1)
            exit()
        else:
            if n * a not in cost:
                cost[n * a] = cost_n + 1
                queue.append(n * a)

print(-1)




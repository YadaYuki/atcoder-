from collections import deque,defaultdict
a,N = map(int,input().split())

if N == 1:
    print(0)
    exit()

BIG = 10 ** 18
costs_to_x = defaultdict(lambda:BIG)
costs_to_x[1] = 0
queue = deque([1])
N_digit_num = len(str(N))

def o1(n:int):
    n_digit_num = len(str(n))
    return (n % 10) * 10 ** (n_digit_num - 1) + n // 10

while len(queue) > 0:
    x = queue.popleft()
    cost_to_x = costs_to_x[x]
    o1x = o1(x)
    o2x = a * x
    # print(x,cost_to_x,o1x,o2x)
    if costs_to_x[o1x] == BIG:
        if x % 10 != 0:
            if o1x== N:
                print(cost_to_x + 1)
                exit()
            else:
                costs_to_x[o1x] = cost_to_x + 1
                queue.append(o1x)
    if costs_to_x[o2x] == BIG:
        if len(str(o2x)) <= N_digit_num:
            if o2x == N:
                print(cost_to_x + 1)
                exit()
            else:
                costs_to_x[o2x] = cost_to_x + 1
                queue.append(o2x)
print(-1)
N = int(input())
A = list(map(int,input().split()))
eps = 1e-7

def f(x):
    cost = 0.0
    for a in A:
        cost += x + a - min(a,2*x)
    return cost

min_x,max_x = 0.0, 1.0 * 10 ** 9
while max_x - min_x > eps:
    l = min_x + (max_x - min_x) / 3 
    r = max_x - (max_x - min_x) / 3 
    if f(r) > f(l):
        # 
        max_x = r
    else:
        min_x = l


print(f(max_x)/N)
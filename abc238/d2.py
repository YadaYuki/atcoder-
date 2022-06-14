def solve_query(a, s):
    return s - 2 * a >= 0 and a & (s-2*a) == 0


T = int(input())

for _ in range(T):
    a, s = map(int, input().split())
    if solve_query(a, s):
        print('Yes')
    else:
        print('No')

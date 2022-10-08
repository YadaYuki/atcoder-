N = int(input())
A = list(map(int, input().split()))

def f(x):
    mean = 0.0
    for a in A:
        mean += x + a -min(a,2*x)
    mean /= N
    return mean


# 3部探索

left = -0.1
right = float(10 ** 9 + 1)

eps = 1e-7

while right - left > eps:
    mid_left = right/3+left*2/3
    mid_right = right*2/3+left/3
    if f(mid_left) >= f(mid_right):
        left = mid_left
    else:
        right = mid_right


print(f(right))
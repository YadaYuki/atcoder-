from bisect import bisect_left


def find_closest_val(lst: list, val: int):
    """
    数列lst内で数値valに最も近い値を二分探索で探し、valとの絶対値の差を返す
    """
    # leftはlst内のval未満でvalに最も近い要素のインデックス
    left = bisect_left(lst, val)
    res = abs(val - lst[left - 1])
    if left < len(lst):
        res = min(res, abs(val - lst[left]))
    return res


N = int(input())
lst = [[] for _ in range(3)]
color = "RGB"
for _ in range(N * 2):
    a, c = input().split()
    lst[color.index(c)].append(int(a))
A, B, C = lst

while len(C) % 2 == 1:  # Cが偶数個の色になるようにA,B,Cの名前を変える
    C, A, B = A, B, C

if len(A) % 2 == 0:     # (A,B,C)=(偶,偶,偶)の場合は答え0
    print(0)
    exit()

# 以降(A,B,C)=(奇,奇,偶)

A.sort()  # 二分探索のためのソート
B.sort()

# A,Bから1つずつ選ぶ場合
ans = min(find_closest_val(B, a) for a in A)

# A,CとB,Cで1つずつ選ぶ場合
if C:
    res = 0
    res += min(find_closest_val(A, c) for c in C)
    res += min(find_closest_val(B, c) for c in C)
    ans = min(ans, res)

print(ans)

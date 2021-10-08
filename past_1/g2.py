N = int(input())
happy_pattern = []
for i in range(N-1):
    item = list(map(int, input().split()))
    happy_pattern.append([0]*(i+1) + item)

happy = [0] * (2 ** N)  # 全ての人の組み合わせに対する幸福度の総和を格納する。


def has_bit(n:int,i:int) -> bool:
    """
    nの右から数えてiビット目が1であるかどうかを返す。
    """
    return n & (1 << i) > 0

# 各グループごとの幸福度を求める

for group in range(2**N):
    happy_sum = 0
    for i in range(0,N-1):
        for j in range(i+1,N):
            if has_bit(group, i) and has_bit(group, j):
                happy_sum += happy_pattern[i][j]
    happy[group] = happy_sum

ans = -float("inf")
# 各組み合わせに応じた幸福度の総和
for g1 in range(2**N):
    for g2 in range(2**N):
        if g1 & g2 > 0:
            continue
        g3 = (2**N - 1) - (g1 | g2)
        ans = max(ans,happy[g1] + happy[g2] + happy[g3])

print(ans)

    

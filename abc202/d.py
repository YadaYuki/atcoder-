A,B,K = map(int,input().split())

pattern_nums = [[0]*(B+1) for _ in range(A+1)] # Aがi=0~Aであった場合,Bがj=0~Bであった場合の並べ方の数

for i in range(A+1):
    for j in range(B+1):
        if i == 0 and j == 0:
            pattern_nums[i][j] = 1
        elif i == 0:
            pattern_nums[i][j] = pattern_nums[i][j-1]
        elif j == 0:
            pattern_nums[i][j] = pattern_nums[i-1][j]
        else:
            pattern_nums[i][j] = pattern_nums[i-1][j] + pattern_nums[i][j-1]


def get_kth_str(a,b,k):
    if a == 0: # Aの数が0
        return ''.join(['b'] * b)
    elif b == 0: # Bの数が0
        return ''.join(['a'] * a)
    else:
        if k <= pattern_nums[a-1][b]: # kが「A=a-1,B=bの時の並べ方よりも小さい時」aが先頭になる.
            return 'a' + get_kth_str(a-1,b,k)
        else:
            return 'b' + get_kth_str(a,b-1,k-pattern_nums[a-1][b])

print(get_kth_str(A,B,K))

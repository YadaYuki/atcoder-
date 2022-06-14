A,B,K = map(int,input().split())

str_pattern_num = [[0]*(B+1) for _ in range(A+1)]
str_pattern_num[0][0] = 1

for i in range(A+1):
    for j in range(B+1):
        if i > 0:
            str_pattern_num[i][j] += str_pattern_num[i-1][j]
        if j > 0:
            str_pattern_num[i][j] += str_pattern_num[i][j-1]

def get_kth_str(a,b,k):
    if a == 0:
        return 'b' * b
    if b == 0:
        return 'a' * a
    if k <= str_pattern_num[a-1][b]: # kが「A=a-1,B=bの時の並べ方よりも小さい時」aが先頭になる.
        return 'a' + get_kth_str(a-1,b,k)
    else:
        return 'b' + get_kth_str(a,b-1,k-str_pattern_num[a-1][b])

print(get_kth_str(A,B,K))



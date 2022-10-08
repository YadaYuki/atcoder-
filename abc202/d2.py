A,B,K = map(int,input().split())

char_order_pattern_num = [[0]*(B+1) for _ in range(A+1)]
char_order_pattern_num[0][0] = 1

for i in range(A+1):
    for j in range(B+1):
        if i == 0 and j == 0:
            char_order_pattern_num[i][j] = 1
        elif i == 0:
            char_order_pattern_num[i][j] = char_order_pattern_num[i][j-1]
        elif j == 0:
            char_order_pattern_num[i][j] = char_order_pattern_num[i-1][j]
        else:
            char_order_pattern_num[i][j] = char_order_pattern_num[i-1][j] + char_order_pattern_num[i][j-1]

def get_kth_str(a,b,k):
    if a == 0:
        return ''.join(['b'] * b)
    if b == 0:
        return ''.join(['a'] * a)
    if k <= char_order_pattern_num[a-1][b] :
        return "a" + get_kth_str(a-1,b,k) 
    else:
        return "b" + get_kth_str(a,b-1,k-char_order_pattern_num[a-1][b])         


print(get_kth_str(A, B, K))

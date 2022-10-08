N = int(input())

S = [list(input()) for _ in range(N)]

# check horizontal
SIX = 6
WHITE,BLACK = '.','#'
is_possible = False
for k in range(N):
    for i in range(N-SIX+1):
        black_count = 0
        for j in range(i,i+SIX):
            if S[k][j] == BLACK:
                black_count += 1
        is_possible = is_possible or black_count >= 4

# check vertical
for k in range(N):
    for i in range(N-SIX+1):
        black_count = 0
        for j in range(i,i+SIX):
            if S[j][k] == BLACK:
                black_count += 1
        is_possible = is_possible or black_count >= 4
        
# check diagonal(left to right)
for k in range(N-SIX+1):
    for i in range(N-SIX+1):
        black_count = 0
        for j in range(SIX):
            if S[k+j][i+j] == BLACK:
                black_count += 1
        is_possible = is_possible or black_count >= 4

# check diagonal(right to left)
for i in range(N-SIX+1):
    for j in range(N-1,SIX-2,-1): # 
        black_count = 0
        for k in range(SIX):
            if S[i+k][j-k] == BLACK:
                black_count += 1
        is_possible = is_possible or black_count >= 4

if is_possible:
    print('Yes')
else:
    print('No')




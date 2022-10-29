N = int(input())
S = list(input())
W = list(map(int,input().split()))

weight_and_adults = [[W[i],S[i]] for i in range(N)]

weight_and_adults.sort()

children = 0
adults = 0
left_children = 0
left_adults = 0

for c in S:
    if c == "1":
        left_adults += 1
    else:
        left_children += 1

ans = left_adults

# 一つ一つ見ていく体重wの数直線における左側にxを据える.
for i in range(N):
    w,c = weight_and_adults[i]
    if c == "1":
        adults += 1
        left_adults-=1
    else:
        children += 1
        left_children -= 1
    
    if i < N-1:
        if weight_and_adults[i][0] == weight_and_adults[i+1][0]:
            # NOTE: 一つ後が同じ値の時は更新しない
            continue
    
    fx = children + left_adults

    ans = max(ans,fx)


print(ans)
    
    

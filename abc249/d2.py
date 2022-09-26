def enum_div(N:int):
    div = []
    for i in range(1,int(N**0.5)+1):
        if N % i == 0:
            div.append(i)
            if i * i != N:
                div.append(N//i)
    return div


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    cnt = [0] * 200001
    for i in range(N):
        cnt[A[i]] += 1
    ans = 0
    for i in range(N):
        A_j_candidates = enum_div(A[i]) # せいぜい160まで

        for A_j in A_j_candidates:
            cnt_j = cnt[A_j]
            cnt_k = cnt[A[i]//A_j]
            ans += cnt_j * cnt_k
    
    enum_div_count = -1
    for i in range(1,200001):
        # print(enum_div(i))
        enum_div_count = max(enum_div_count,len(enum_div(i)))
    
    
    
    print(ans)



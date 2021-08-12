
import itertools

if __name__ == "__main__":
    N,M,Q = map(int,input().split())
    num_arr = []
    for i in range(Q):
        num_arr.append(list(map(int,input().split())))
    # dfs([1,1],N,M,Q,num_arr)
    pattern_arr = list(itertools.combinations_with_replacement([i for i in range(1,M+1)],N))
    ans = 0
    for pattern in pattern_arr:
        d_sum = 0
        pattern = [1] + list(pattern)
        for i in range(Q):
            if pattern[num_arr[i][1]-1] - pattern[num_arr[i][0]-1] == num_arr[i][2]:
                d_sum += num_arr[i][3]
        ans = max(ans,d_sum)
    print(ans)

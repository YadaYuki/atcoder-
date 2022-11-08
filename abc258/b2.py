
N = int(input())
A = [list(list(input())) for _ in range(N)]

def next_idx(c_idx):
    return c_idx + 1 if c_idx + 1 < N else 0


def prev_idx(c_idx):
    return c_idx - 1 if c_idx - 1 >= 0 else N - 1
ans = -1
for si in range(N):
    for sj in range(N):
        # (0,+1)
        num_str = ""
        i,j = si,sj
        for _ in range(N):
            num_str += A[i][j]
            i = next_idx(i)
        
        ans = max(ans,int(num_str))

        # (+1,0)
        num_str = ""
        i,j = si,sj
        for _ in range(N):
            num_str += A[i][j]
            j = next_idx(j)
        
        ans = max(ans,int(num_str))

        # (+1,+1)
        num_str = ""
        i,j = si,sj
        for _ in range(N):
            num_str += A[i][j]
            i = next_idx(i)
            j = next_idx(j)
        
        ans = max(ans,int(num_str))

        # (0,-1)
        num_str = ""
        i,j = si,sj
        for _ in range(N):
            num_str += A[i][j]
            j = prev_idx(j)
        
        ans = max(ans,int(num_str))

        # (-1,0)
        num_str = ""
        i,j = si,sj
        for _ in range(N):
            num_str += A[i][j]
            i = prev_idx(i)
        
        ans = max(ans,int(num_str))

        # (-1,-1)
        num_str = ""
        i,j = si,sj
        for _ in range(N):
            num_str += A[i][j]
            i = prev_idx(i)
            j = prev_idx(j)
        
        ans = max(ans,int(num_str))
        
        # (+1,-1)
        num_str = ""
        i,j = si,sj
        for _ in range(N):
            num_str += A[i][j]
            i = next_idx(i)
            j = prev_idx(j)
        
        ans = max(ans,int(num_str))

        # (-1,+1)
        num_str = ""
        i,j = si,sj
        for _ in range(N):
            num_str += A[i][j]
            i = prev_idx(i)
            j = next_idx(j)
        
        ans = max(ans,int(num_str))


print(ans)
N = int(input())
A = [list(map(int,list(input()))) for _ in range(N)]

def next_cordinate(cur):
    return 0 if cur == N - 1 else cur + 1

def prev_cordinate(cur):
    return N - 1 if cur == 0 else cur - 1

ans = -1
for si in range(N):
    for sj in range(N):
        # (0,+1)
        num_str = ""
        i,j = si,sj
        for _ in range(N):
            num_str += str(A[i][j])
            j = next_cordinate(j)
        ans = max(ans,int(num_str))
        # (+1,0)
        num_str = ""
        i,j = si,sj
        for _ in range(N):
            num_str += str(A[i][j])
            i = next_cordinate(i)
        ans = max(ans,int(num_str))
        # (+1,+1)
        num_str = ""
        i,j = si,sj
        for _ in range(N):
            num_str += str(A[i][j])
            i = next_cordinate(i)
            j = next_cordinate(j)
        ans = max(ans,int(num_str))
        # print(si,sj,int(num_str))
        # (0,-1)
        num_str = ""
        i,j = si,sj
        for _ in range(N):
            num_str += str(A[i][j])
            j = prev_cordinate(j)
        ans = max(ans,int(num_str))
        # (-1,0)
        num_str = ""
        i,j = si,sj
        for _ in range(N):
            num_str += str(A[i][j])
            i = prev_cordinate(i)
        ans = max(ans,int(num_str))
        # (-1,-1)
        num_str = ""
        i,j = si,sj
        for _ in range(N):
            num_str += str(A[i][j])
            i = prev_cordinate(i)
            j = prev_cordinate(j)
        ans = max(ans,int(num_str))
        # (-1,+1)
        num_str = ""
        i,j = si,sj
        for _ in range(N):
            num_str += str(A[i][j])
            i = prev_cordinate(i)
            j = next_cordinate(j)
        ans = max(ans,int(num_str))
        # (+1,-1)
        num_str = ""
        i,j = si,sj
        for _ in range(N):
            num_str += str(A[i][j])
            i = next_cordinate(i)
            j = prev_cordinate(j)
        ans = max(ans,int(num_str))
        # print(si,sj)
print(ans)
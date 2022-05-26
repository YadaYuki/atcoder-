N,W = map(int,input().split())
A = list(map(int,input().split()))
cnts_of_times_in_line = []  # [(各作業員のID,各作業員が列に並ぶ回数),... ]
for i in range(N):
    cnt_of_times_in_line = - (-A[i] // W)
    cnts_of_times_in_line.append((i+1,cnt_of_times_in_line))

cnts_of_times_in_line.sort(key=lambda x:(x[1],x[0]))

for ans in cnts_of_times_in_line:
    print(ans[0])

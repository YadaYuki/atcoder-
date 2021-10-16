N = int(input())
tasks = []

for _ in range(N):
    a,b = map(int,input().split())
    tasks.append((b,a))


tasks.sort()

B,A = tasks[0]
cur_task_B = B
ans = 1
for i in range(1,N):
    B,A = tasks[i]
    if cur_task_B < A: # タスクを行う
        ans += 1
        cur_task_B = B

print(ans)
    
    

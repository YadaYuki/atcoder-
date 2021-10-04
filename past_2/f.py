N = int(input())
enable_task_in_d = []
for i in range(N):
    enable_task_in_d.append([])

for i in range(N):
    A, B = map(int, input().split())
    enable_task_in_d[A-1].append(B)

enable_task_point = [0] * 101


ans = 0
for d in range(N):
    for task_point in enable_task_in_d[d]:
        enable_task_point[task_point] += 1
    for i in range(100,-1,-1):
        if enable_task_point[i] > 0:
            enable_task_point[i] -= 1
            ans += i
            print(ans)
            break

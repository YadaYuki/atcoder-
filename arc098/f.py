from collections import defaultdict

N = int(input()) 

points = [0 for _ in range(101)]

task_day_dict = defaultdict(list) # {(日付):[ポイントの配列...]}


for _ in range(N):
    A,B = map(int,input().split())
    task_day_dict[A-1].append(B)


max_point_sum_in_k = 0

for k in range(N):
    enable_task_list_in_k = task_day_dict[k]
    
    for item in enable_task_list_in_k:
        points[item] = points[item] + 1

    max_point_in_k = -1

    for point in range(100,-1,-1):
        if points[point] > 0:
            max_point_in_k = point
            points[point] = points[point] - 1
            break
    
    max_point_sum_in_k += max_point_in_k
    print(max_point_sum_in_k)



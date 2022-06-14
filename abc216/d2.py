from collections import deque
N,M = map(int,input().split())

cylinders = []

for i in range(M):
    k = int(input())
    a = list(map(int, input().split()))
    cylinders.append(a)

cylinder_idx_ls = [[] for i in range(N + 1)]
ball_has_pair_in_head = deque()


for i in range(M):
    head = cylinders[i][-1]
    cylinder_idx_ls[head].append(i)
    if len(cylinder_idx_ls[head]) == 2:
        ball_has_pair_in_head.append(head)


while len(ball_has_pair_in_head) > 0:
    ball_has_pair = ball_has_pair_in_head.popleft()
    pair_cylinder_idx_ls = cylinder_idx_ls[ball_has_pair][:]
    for cylinder_idx in pair_cylinder_idx_ls:
        cylinders[cylinder_idx].pop()
        if len(cylinders[cylinder_idx]) > 0:
            new_head = cylinders[cylinder_idx][-1]
            
            cylinder_idx_ls[new_head].append(cylinder_idx)
            if len(cylinder_idx_ls[new_head]) == 2:
                ball_has_pair_in_head.append(new_head)
                


for i in range(1,len(cylinder_idx_ls)):
    if len(cylinder_idx_ls[i]) != 2:
        print("No")
        exit()
print("Yes")

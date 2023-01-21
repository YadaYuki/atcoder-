N,M = map(int,input().split())
A = list(map(int,input().split()))
op_cnt_to_important_num = [set() for i in range(M)]

for idx,a in enumerate(A):
    i = idx + 1
    if a + i > N:
        continue
    
    min_op_cnt_to_important_num,min_important_num = None,None
    if a < 0:
        min_op_cnt_to_important_num = ((-a) // i) + 1
        if (-a) % i == 0:
            min_op_cnt_to_important_num -= 1
        min_important_num = min_op_cnt_to_important_num * i + a
    else:
        min_op_cnt_to_important_num = 1
        min_important_num = a + i
    op_cnt = min_op_cnt_to_important_num
    important_num = min_important_num

    while op_cnt <= M and important_num <= N:
        op_cnt_to_important_num[op_cnt-1].add(important_num)
        op_cnt += 1
        important_num += i
for i in range(M):
    ans = 0
    while ans in op_cnt_to_important_num[i]:
        ans += 1
    print(ans)



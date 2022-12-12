N,M = map(int,input().split())
A = list(map(int,input().split()))

important_numbers_for_M = [set() for i in range(M)]

for i,a in enumerate(A):
    i = i + 1
    min_important_number = None
    op_cnt_to_important_number = None
    if a > N:
        continue

    if 0 > a:
        op_cnt_to_important_number = (0-a) // i + 1
        if (0-a) % i == 0:
            op_cnt_to_important_number -= 1
        min_important_number = a + op_cnt_to_important_number * i
    else:
        op_cnt_to_important_number = 1
        min_important_number = a + i

    important_number = min_important_number
    while op_cnt_to_important_number <= M:
        if important_number > N:
            break
        important_numbers_for_M[op_cnt_to_important_number-1].add(important_number)
        op_cnt_to_important_number += 1
        important_number += i


for i in range(M):
    ans = 0
    while ans in important_numbers_for_M[i]:
        ans += 1
    print(ans)

# N = int(input())
# A = list(map(int,input().split()))
# max_score = -1
# min_score = 3 * 10 ** 5 + 1
# one_cnt = 0
# zero_cnt = 0
# t1,t2 = 0,0
# for i in range(N):
#     if A[i] == 1:
#         one_cnt += 1
#     else:
#         zero_cnt += 1
    
#     max_score = max(max_score,(zero_cnt - one_cnt) - t1)
#     t1 = max(t1,zero_cnt - one_cnt)
#     min_score = min(min_score,(zero_cnt - one_cnt) - t2)
#     t2 = max(t2,one_cnt - zero_cnt)
    
# print(max_score - min_score + 1)


N = int(input())
A = list(map(int, input().split()))
 
a1 = a2 = t1 = t2 = cnt = 0
for i in range(N):
    if A[i]:
        cnt += 1
    else:
        cnt -= 1
    a1 = max(a1, cnt-t1)
    t1 = min(t1, cnt)
    a2 = min(a2, cnt-t2)
    t2 = max(t2, cnt)
 
print(a1-a2+1)
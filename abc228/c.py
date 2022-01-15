N,K = map(int,input().split())
P = []

point_by_3days = []

for i in range(N):
    point_by_3days.append([sum(list(map(int,input().split()))),i])

point_by_3days.sort(reverse=True)

ans = [False for _ in range(N)] # 生徒iがK位以内に入るかどうか

# 3日目までで、K位以内の生徒は確実に上位K位に入る.
# 3日目までで、同じ点数の人がいたら...どうなる？
for i in range(K): 
    _,student = point_by_3days[i]
    ans[student] = True

#TODO: if K < N and 

K_th_student_point = point_by_3days[K-1][0]

for i in range(K,N):
    p,student = point_by_3days[i]
    if K_th_student_point - p <= 300: #K番目の生徒との得点差が300点以上であった場合、K番目の生徒が0点,studentが満点(300点)であっても逆転できない
        ans[student] = True
    
for i in range(N):
    if ans[i]:
        print("Yes")
    else:
        print("No")



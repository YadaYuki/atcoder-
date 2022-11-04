N,X,Y,Z = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

scores = [] # [student_id,math,english,total]

for i in range(N):
    scores.append([i+1,A[i],B[i],A[i] + B[i]])

scores.sort(key=lambda item:[item[1],-item[0]],reverse=True)

ans = scores[:X]

scores = scores[X:]

scores.sort(key=lambda item:[item[2],-item[0]],reverse=True)

ans.extend(scores[:Y])

scores = scores[Y:]

scores.sort(key=lambda item:[item[3],-item[0]],reverse=True)

ans.extend(scores[:Z])

ans.sort()

for a in ans:
    print(a[0])


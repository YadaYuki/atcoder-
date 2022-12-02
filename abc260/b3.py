N,X,Y,Z = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

scores = [] # [[math,eng,math+eng],[math,eng,math+eng]...]

for i in range(N):
    scores.append([A[i],B[i],A[i] + B[i],i])

admitted = set()

scores.sort(key=lambda item: [-item[0],item[3]])

passed,i = 0,0
while passed < X:
    student_id = scores[i][3]
    if student_id not in admitted:
        admitted.add(student_id)
        passed += 1
    i += 1

scores.sort(key=lambda item: [-item[1],item[3]])

passed,i = 0,0
while passed < Y:
    student_id = scores[i][3]
    if student_id not in admitted:
        admitted.add(student_id)
        passed += 1
    i += 1

scores.sort(key=lambda item: [-item[2],item[3]])

passed,i = 0,0
while passed < Z:
    student_id = scores[i][3]
    if student_id not in admitted:
        admitted.add(student_id)
        passed += 1
    i += 1

admitted = list(admitted)

admitted.sort()
for i in admitted:
    print(i+1)
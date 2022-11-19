N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

students = [
    [i, A[i], B[i], A[i] + B[i]] for i in range(N)
]

passed = set()

students.sort(key=lambda item: [-item[1],item[0]])

i,x = 0,0
while x < X:
    if not (students[i][0] in passed):
        passed.add(students[i][0])
        x += 1
    i+=1

students.sort(key=lambda item: [-item[2],item[0]])
i,y = 0,0
while y < Y:
    if not (students[i][0] in passed):
        passed.add(students[i][0])
        y += 1
    i+=1

students.sort(key=lambda item: [-item[3],item[0]])
i,z = 0,0
while z < Z:
    if not (students[i][0] in passed):
        passed.add(students[i][0])
        z += 1
    i+=1

passed = list(passed)
passed.sort()

for i in passed:
    print(i+1)
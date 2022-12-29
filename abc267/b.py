S = list(map(int,list(input())))

if S[0] != 0:
    print("No")
    exit()

row = [
    [6],
    [3],
    [1,7],
    [0,4],
    [2,8],
    [5],
    [9]
]

is_all_falled = [False for i in range(len(row))]
for i in range(len(row)):
    is_all_falled[i] = True
    for p in row[i]:
        if S[p] == 1:
            is_all_falled[i] = False
            break


for i in range(0,len(row)-2):
    for j in range(i+2,len(row)):
        for r in range(i+1,j):
            if is_all_falled[i] == False and is_all_falled[j] == False and is_all_falled[r] == True:
                print("Yes")
                exit()
print("No")


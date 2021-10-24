N = int(input())
Q = int(input())
row = [i for i in range(N)]
column = [i for i in range(N)]
is_transposition = False

ans = []

for _ in range(Q):
    query = input().split()
    if query[0] == "3":
        is_transposition = not is_transposition
        column,row = row,column
    else:
        num, A, B = map(int, query)
        A -= 1
        B -= 1
        if num == 1:
            row[A], row[B] = row[B], row[A]
        elif num == 2:
            column[A], column[B] = column[B], column[A]
        else:
            i, j = row[A], column[B]
            if is_transposition:
                i, j = j, i
            ans.append(N*i+j)
for i in range(len(ans)):
    print(ans[i])

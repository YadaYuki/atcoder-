A,R,N = map(int,input().split())

if R == 1:
    print(A)
else:
    for i in range(N-1):
        A *= R
        if A > 10 ** 9:
            print("large")
            exit()
    print(A)


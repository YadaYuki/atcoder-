A,R,N = map(int,input().split())

MAX_NUM = 10 ** 9

if R == 1:
    print(A)
else:
    for i in range(0,N-1):
        A *= R
        if A > MAX_NUM: # A * (R ** i-1)がi項目の値。
            print("large")
            exit()
    print(A)
    

A,B,C,X = map(int,input().split())

if X <= A:
    print(float(1))
elif A + 1 <= X <= B:
    print(C/(B - A))
else:
    print(0.0)


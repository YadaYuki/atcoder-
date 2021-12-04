H,W,N = map(int,input().split())

X,Y = [],[]
X_dict,Y_dict = {},{}

for i in range(N):
    A,B = map(int,input().split())
    X_dict[A] = -1
    Y_dict[B] = -1
    X.append(A)
    Y.append(B)


X_sorted = sorted(X)
Y_sorted = sorted(Y)

for i in range(N):
    X_dict[X_sorted[i]] = i
    Y_dict[Y_sorted[i]] = i

for i in range(N):
    print(f'{X_dict[X[i]]+1} {Y_dict[Y[i]]+1}')




X,Y,Z = map(int,input().split())
coordinates = [[0,"0"],[X,"X"],[Y,"Y"],[Z,"Z"]]
coordinates.sort()
zero_idx = coordinates.index([0,"0"])
X_idx = coordinates.index([X,"X"])
Y_idx = coordinates.index([Y,"Y"])
Z_idx = coordinates.index([Z,"Z"])

if abs(X_idx-zero_idx) == 1:
    print(abs(X))
elif (zero_idx < Y_idx < Z_idx) or (Z_idx < Y_idx < zero_idx):
    print(-1)
elif (X_idx < Y_idx < zero_idx < Z_idx) or (Z_idx < zero_idx < Y_idx < X_idx):
    print(abs(X) + abs(Z) * 2)
else:
    print(abs(X))


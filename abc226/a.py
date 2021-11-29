import math

X_str = input()
X = math.floor(float(X_str))
if int(X_str.split(".")[1][0]) >= 5:
    print(X+1)
    exit(0)
print(X)






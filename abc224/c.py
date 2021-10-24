coordinates = []
N = int(input())

for _ in range(N):
    X,Y = map(int,input().split())
    coordinates.append([X,Y])

def is_line(a,b,c):
    x1,y1 = a
    x2,y2 = b
    x3,y3 = c
    if x1 == x2 or x2 == x3:
        if x1 == x2 and x2 == x3: # x座標が全て同じ場合以外は一直線ではない。
            return True
        return False
    return (y2-y1)/(x2-x1) == (y3-y2)/(x3-x2)

ans = 0

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            a,b,c = coordinates[i],coordinates[j],coordinates[k]
            if not is_line(a, b, c):
                ans += 1


print(ans)

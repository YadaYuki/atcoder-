A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
D = list(map(int,input().split()))

def cross_product(v1,v2):
    return v1[0]*v2[1] - v2[0]*v1[1]

vertexes = [A,B,C,D]
v_cnt = len(vertexes)
for i in range(v_cnt):
    a,b,c = vertexes[i%v_cnt],vertexes[(i+1)%v_cnt],vertexes[(i+2)%v_cnt]

    a2b = [b[0]-a[0], b[1]-a[1]]
    b2c = [c[0]-b[0], c[1]-b[1]]
    if cross_product(a2b, b2c) < 0:
        print("No")
        exit()
print("Yes")
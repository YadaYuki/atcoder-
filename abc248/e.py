from collections import defaultdict
N,K = map(int,input().split())
coordinates = [tuple(map(int,input().split())) for _ in range(N)]


def calculate_slop(a,b):
    xa,ya = a
    xb,yb = b
    if xa == xb:
        return "inf"
    if yb==ya:
        return 0.0
    return (yb-ya)/(xb-xa)

def calculate_intercept(a,b):
    xa,ya = a
    xb,yb = b
    if xa == xb:
        return "inf"
    return ya - (calculate_slop(a,b)*xa)


def get_line_str(a,b):
    slope = calculate_slop(a,b)
    intercept = calculate_intercept(a,b)
    if slope == "inf":
        xa = a[0]
        return "x={}".format(xa)
    return "y={}x+{}".format(slope,intercept)


if K == 1:
    print("Infinity")
else:
    lines_dict = {} # {coordinate: set{linestr}}
    for i in range(N-1):
        for j in range(i+1,N):
            a = coordinates[i]
            b = coordinates[j]
            line_str = get_line_str(a,b)
            if a not in lines_dict:
                lines_dict[a] = set()
            if b not in lines_dict:
                lines_dict[b] = set()
            lines_dict[a].add(line_str)
            lines_dict[b].add(line_str)
    
    lin_dict = defaultdict(int)

    for key,lines in lines_dict.items():
        for line in lines:
            lin_dict[line] += 1
    ans = 0
    for line in lin_dict:
        if lin_dict[line] >= K:
            ans += 1

    print(ans)
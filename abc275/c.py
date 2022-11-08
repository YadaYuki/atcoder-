S = [list(input()) for _ in range(9)]


def idx_to_coordinate(idx):
    return [idx // 9, idx % 9]

def is_square(a,b,c,d):
    dots = [a,b,c,d]
    v = []
    for i in range(4):
        for j in range(i+1,4):
            xi,yi = dots[i]
            xj,yj = dots[j]
            dx = xi-xj
            dy = yi-yj
            v.append(dx**2 + dy ** 2)
    l = v[0]
    v.sort()

    return (v[0] == l) and (v[1] == l) and (v[2] == l) and (v[3] == l) and (v[4] == 2*l) and (v[5] == 2*l)
ans = 0
for i in range(0,78):
    for j in range(i+1,79):
        for k in range(j+1,80):
            for l in range(k+1,81):
                ci = idx_to_coordinate(i)
                cj = idx_to_coordinate(j)
                ck = idx_to_coordinate(k)
                cl = idx_to_coordinate(l)
                if S[ci[0]][ci[1]] == "#" and S[cj[0]][cj[1]] == "#" and S[ck[0]][ck[1]] == "#" and S[cl[0]][cl[1]] == "#":
                    if is_square(ci, cj, ck, cl):
                        ans += 1




print(ans)
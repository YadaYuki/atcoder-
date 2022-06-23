h1,h2,h3,w1,w2,w3 = map(int,input().split())


mat = [[0,0,0],[0,0,0],[0,0,0]]

elem_candidate = [i for i in range(1,29)]
ans = 0
for a in elem_candidate:
    for b in elem_candidate:
        for c in elem_candidate:
            for d in elem_candidate:
                
                mat[0][0] = a
                mat[0][1] = b
                mat[0][2] = h1 - (a+b)
                mat[1][0] = c
                mat[1][1] = d
                mat[1][2] = h2 - (c+d)
                mat[2][0] = w1 - (a+c)
                mat[2][1] = w2 - (b+d)
                if not ((w3 - (mat[0][2] + mat[1][2])) == (h3 - (mat[2][0] + mat[2][1]))):
                    
                    continue
                else:
                    mat[2][2] = w3 - (mat[0][2] + mat[1][2])
                
                ok = True
                for i in range(3):
                    for j in range(3):
                        if mat[i][j] < 1:
                            ok = False
                ans += ok



print(ans)
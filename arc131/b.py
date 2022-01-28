H,W = map(int,input().split())
cambus = [list(input()) for _ in range(H)]
visited = [[False]*W for _ in range(H)]

color_pattern = [i for i in range(1,6)]


def dfs(h,w):
    visited[h][w] = True
    
    is_top = h == 0
    is_bottom = h == H-1
    is_left = w == 0
    is_right = w == W-1

    # h,wに色を塗るx
    if cambus[h][w] == '.':

        u,d,l,r = None,None,None,None

        if not is_top:
            u = cambus[h-1][w]
        if not is_bottom:
            d = cambus[h+1][w]
        if not is_left:
            l = cambus[h][w-1]
        if not is_right:
            r = cambus[h][w+1]

        color_next_to = {u,d,l,r}

        for color in color_pattern:
            if str(color) not in color_next_to:
                cambus[h][w] = str(color)
                break


    next_h_ok = not is_bottom
    if next_h_ok:
        next_h_ok = visited[h+1][w] == False
    
    next_w_ok = not is_right
    if next_w_ok:
        next_w_ok = visited[h][w+1] == False

    if next_h_ok:
        dfs(h+1,w)
    if next_w_ok:
        dfs(h,w+1)
    

dfs(0,0)

for i in range(H):
    print(''.join(cambus[i]))


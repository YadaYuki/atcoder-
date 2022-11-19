N,X,Y = map(int,input().split())

BLUE,RED = "BLUE","RED"

def blue_cnt(color,level,cnt):
    if level == 1:
        if color == BLUE:
            return cnt
        else:
            return 0
    
    if color == RED:
        return blue_cnt(RED, level-1, cnt) + blue_cnt(BLUE, level, cnt * X)
    elif color == BLUE:
        return blue_cnt(RED, level-1, cnt) + blue_cnt(BLUE, level-1, cnt * Y)

print(blue_cnt(RED, N, 1))
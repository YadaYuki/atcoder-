RED, BLUE = "RED", "BLUE"
N, X, Y = map(int, input().split())


def get_blue_cnt(color: str, cnt: int, level: int):
    if level == 1:
        if color == BLUE:
            return cnt
        else:
            return 0
    else:
        if color == BLUE:
            return get_blue_cnt(RED, cnt, level-1) + get_blue_cnt(BLUE, cnt * Y, level-1)
        elif color == RED:
            return get_blue_cnt(RED, cnt, level-1) + get_blue_cnt(BLUE, cnt * X, level)

print(get_blue_cnt(RED, 1, N))
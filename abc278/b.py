H,M = map(int,input().split())

def is_misjudge(h,m):
    hs,ms = list(str(h).zfill(2)),list(str(m).zfill(2))
    right_up = ms[0]
    left_down = hs[1]
    hs[1] = right_up
    ms[0] = left_down
    h_changed = int("".join(hs))
    m_changed = int("".join(ms))
    # print(h_changed,m_changed)
    return (0 <= h_changed <= 23) and (0 <= m_changed <= 59)

h,m = H,M
time_minutes = h * 60 + M
while not is_misjudge(h, m):
    if time_minutes >= 1440:
        h,m = 0,0
        time_minutes = 0
    else:
        h = time_minutes // 60
        m = time_minutes % 60
        time_minutes += 1


print(h,m)
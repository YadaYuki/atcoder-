# 外部サイトは調べずに尺取り法をやってみる
N,P,Q,R = map(int,input().split())
A = list(map(int,input().split()))

def get_section_pair(section_sum:int):
    cur_sum = 0
    tail = 0
    section_pair = {}
    for head in range(N):
        while (tail < N) and (cur_sum < section_sum):
            cur_sum += A[tail]
            tail += 1
        if cur_sum == section_sum:
            section_pair[head] = tail - 1
        cur_sum -= A[head]
    
    return section_pair

p_pair,q_pair,r_pair = get_section_pair(P),get_section_pair(Q),get_section_pair(R)

for ph,pt in p_pair.items():
    if (pt+1) in q_pair:
        qh,qt = pt+1,q_pair[pt+1]
        if (qt+1) in r_pair:
            print("Yes")
            exit()
print("No")
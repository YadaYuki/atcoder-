from collections import defaultdict
N = int(input())
p = list(map(int,input().split()))
dish_to_pos = [-1 for i in range(N)]
for i,p in enumerate(p):
    dish_to_pos[p] = i

p_to_happy_cycle_cnt = [None for i in range(N)]
for p in range(N):
    dish_pos = dish_to_pos[p]
    cycle = (p - dish_pos) % N
    p_to_happy_cycle_cnt[p] = [(cycle-1)%N,cycle,(cycle+1)%N]

cycle_cnt_to_happy_num = defaultdict(int)

for happy_cycle_cnts in p_to_happy_cycle_cnt:
    for happy_cycle_cnt in happy_cycle_cnts:
        cycle_cnt_to_happy_num[happy_cycle_cnt] += 1


ans = -1
for k,v in cycle_cnt_to_happy_num.items():
    ans = max(ans,v)
print(ans)
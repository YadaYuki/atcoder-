from collections import defaultdict
N,M = map(int,input().split())
S = input().split()
T = input().split()
stations_express_stop_map = defaultdict(bool)
for station in T:
    stations_express_stop_map[station] = True

for i in range(N):
    if S[i] in stations_express_stop_map:
        print('Yes')
    else:
        print('No')
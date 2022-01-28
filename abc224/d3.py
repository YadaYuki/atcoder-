from collections import deque,defaultdict

M = int(input())
G = [[] for _ in range(9)]
for _ in range(M):
    u,v = map(int,input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)

p = list(map(int,input().split())) # 各コマがどの頂点に存在するか

# 初期状態を文字列で表現
initial_coma_place = ["0"] * 9 # 各頂点にどのコマが存在するか

for i in range(8):
    initial_coma_place[p[i]-1] = str(i+1)

initial_coma_place = "".join(initial_coma_place)

coma_place_dict = defaultdict(bool) # 訪問済みの状態を辞書で管理

Q = deque()
Q.append(initial_coma_place)
count = 0
cost_to_coma = {} # 各並び順に至るまでのコストを連想配列で管理
cost_to_coma[initial_coma_place] = 0

if initial_coma_place == "123456780":
    print(0)
    exit()

while len(Q) > 0:
    coma_place = Q.popleft()
    # 隣接する駒の状態を列挙する
    empty_coma_place = coma_place.index("0") # 空・コマがない頂点の位置
    cost_to_next_coma = cost_to_coma[coma_place] + 1
    coma_place_list = list(coma_place)
    for i in G[empty_coma_place]:
        coma_place_next_to = coma_place_list[:]
        coma_place_next_to[i],coma_place_next_to[empty_coma_place] = coma_place_next_to[empty_coma_place],coma_place_next_to[i]
        coma_place_next_to = "".join(coma_place_next_to)
        if coma_place_next_to == '123456780':
            print(cost_to_next_coma)
            exit()
        if coma_place_next_to not in coma_place_dict:
            coma_place_dict[coma_place_next_to] = True
            Q.append(coma_place_next_to)
            cost_to_coma[coma_place_next_to] = cost_to_next_coma
        
print(-1)
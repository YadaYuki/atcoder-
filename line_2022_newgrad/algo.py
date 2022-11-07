from collections import deque,defaultdict
import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    N,M,Q = map(int,lines[0].split())

    board_restrictions = [[set() for _ in range(M)] for _ in range(N)] # TODO: 複数にも対応
    for i in range(1,Q+1):
        s,t,x = map(int,lines[i].split())
        board_restrictions[s][t].add(x)

    # BFS
    queue = deque([])
    cost = {}
    visited = defaultdict(bool)

    # init
    initial_dice_state = (1,4,3,2,5,6) # [top,east,west,south,north,bottom]
    initial_coordinate = (0,0)
    initial_state = (initial_coordinate,initial_dice_state)

    queue.append(initial_state)
    cost[initial_state] = 0
    visited[initial_state] = True

    while len(queue) > 0:
        cur = queue.popleft()
        coordinate,dice_state = cur
        i,j = coordinate
        top,east,west,south,north,bottom = dice_state
        nexts = [
            ((i+1,j),(north,east,west,top,bottom,south)), # 南
            ((i-1,j),(south,east,west,bottom,top,north)), # 北
            ((i,j+1),(west,top,bottom,south,north,east)), # 東
            ((i,j-1),(east,bottom,top,south,north,west)), # 西
        ]

        for n in nexts:
            nc,nd = n
            ni,nj = nc

            if ni < 0 or nj < 0:
                continue

            if ni >= N or nj >= M:
                continue

            top = nd[0]
            if top in board_restrictions[ni][nj]:
                continue

            if visited[n]:
                continue

            if ni == N - 1 and nj == M - 1:
                print("YES")
                print(cost[cur] + 1)
                exit(0)

            visited[n] = True
            cost[n] = cost[cur] + 1
            queue.append(n)

    print("NO")

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)

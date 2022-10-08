T = int(input())

def solve_query(N,A,B,X,Y,Z):
    costs = [[1,X,X],[A,Y,Y/A],[B,Z,Z/B]] # [一操作で移動できる距離, 操作あたりのコスト, 1移動あたりのコスト]
    costs.sort(key=lambda item: item[2])
    total_cost = 0
    for cost in costs:
        d,c,_ = cost
        total_cost += (N//d) * c
        N = N % d
    return total_cost
ans = []
for _ in range(T):
    N,A,B,X,Y,Z = map(int,input().split())
    ans.append(solve_query(N, A, B, X, Y, Z))

for i in ans:
    print(i)
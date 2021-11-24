# import heapq

# N = int(input())

# graph = [[] for i in range(N)]

# for i in range(N-1):
#     A,B = map(int,input().split())
#     heapq.heappush(graph[A-1], B-1)
#     heapq.heappush(graph[B-1], A-1)



# cur_city = 0
# visited = [False for _ in range(N)]
# visited[0] = True
# prev_visited = [-1 for _ in range(N)]
# ans = [cur_city]

# print(graph)
# while cur_city != 0 or len(graph[0]) != 0:
#     if len(graph[cur_city]) == 0:
#         cur_city = prev_visited[cur_city]
#         ans.append(cur_city)
#     else:
#         prev_city = cur_city
#         cur_city_temp = heapq.heappop(graph[cur_city])
#         if not visited[cur_city_temp]:
#             cur_city = cur_city_temp
#             prev_visited[cur_city] = prev_city
#             ans.append(cur_city)
#         print()
#     print(ans)


# for i in range(len(ans)):
#     print(ans[i] + 1,end=" ")
# おまじない
import sys
sys.setrecursionlimit(300000)
 
N=int(input())
G=[[] for i in range(N+1)]
for i in range(N-1):
  a,b=map(int,input().split())
  G[a].append(b)
  G[b].append(a)
 
for i in range(N+1):G[i].sort()
 
ans=[]
def dfs(crr,pre):
  ans.append(crr)
  for nxt in G[crr]:
    if nxt!=pre:
      dfs(nxt,crr)
      ans.append(crr)
 
dfs(1,-1)
print(*ans)



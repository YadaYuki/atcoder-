from collections import deque
M = int(input())

NODE_NUM = 9
graph = [[] for _ in range(NODE_NUM)]

for _ in range(M):
    u,v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)


EMPTY_STATE = '9'
goal = '123456789'
p = list(map(int,input().split()))
initial_state = ['9'] * NODE_NUM

for j in range(len(p)):
    initial_state[p[j]-1] = str(j+1)

initial_state = ''.join(initial_state)

if initial_state == goal:
    print(0)
    exit()

cost_to_state = {initial_state:0}
queue = deque([initial_state])

def get_next_states(cur_state:str):
    next_states = []
    cur_state_list = list(cur_state)
    empty_state_node = cur_state_list.index(EMPTY_STATE)
    for next_node in graph[empty_state_node]:
        next_state = cur_state_list[:]
        next_state[empty_state_node] = next_state[next_node]
        next_state[next_node] = EMPTY_STATE
        next_state = ''.join(next_state)
        next_states.append(next_state)
    return next_states
        
while len(queue) > 0:
    cur_state = queue.popleft()
    next_states = get_next_states(cur_state)
    cost_to_next_states = cost_to_state[cur_state] + 1
    for next_state in next_states:
        if next_state not in cost_to_state:
            if next_state == goal:
                print(cost_to_next_states)
                exit()
            cost_to_state[next_state] = cost_to_next_states
            queue.append(next_state)
            
        pass


print(-1)
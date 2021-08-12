def dfs(n,graph,start_node):
    stack = [start_node]
    next_node_idx_arr = [0 for _ in range(n)]
    find_idx_arr,searched_idx_arr = [-1 for _ in range(n)],[-1 for _ in range(n)]
    idx = 0
    # TODO: Fix Bug
    # find_
    # stack.append(start_node)
    while len(stack) > 0:
        top = stack[-1]
        # is exist not found node in neighbors

        if len(graph[top]) <= next_node_idx_arr[top]:
            # not exist
            searched_idx_arr[stack.pop()] = idx
        else :
            # todo: fix bug
            # exist
            stack.append(graph[top][next_node_idx_arr[top]])
            find_idx_arr[top] = idx
            next_node_idx_arr[top] += 1
        idx += 1

    return {"find_idx_arr":find_idx_arr,"searched_idx_arr":searched_idx_arr}

if __name__ == "__main__":
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(lambda i: int(i)-1,input().split()[2:])))
    print(graph)


    start_node = 0
    # return : {find_idx_arr:[...],searched_idx_arr:[...]}
    print(dfs(n,graph,start_node))
    
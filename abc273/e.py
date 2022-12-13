class TreeNode:
    def __init__(self,parent:int,value:int):
        self.parent = parent
        self.value = value
        self.children = []
    
    def add_children(self,c):
        self.children.append(c)
    


class Tree:
    def __init__(self):
        self.tree:list[TreeNode] = []
    

    def insert_node(self,value,parent):
        n = TreeNode(parent, value)
        self.tree.append(n)
        inserted_node_idx = len(self.tree) - 1
        self.tree[parent].add_children(inserted_node_idx)
        return inserted_node_idx

if __name__ == "__main__":
    Q = int(input())
    t = Tree()
    
    note = {}
    ans = []
    cur = t.insert_node(-1, 0)
    for i in range(Q):
        query = input().split()
        q = query[0]
        if q == "ADD":
            x = int(query[1])
            cur = t.insert_node(x, cur)
        if q == "DELETE":
            cur = t.tree[cur].parent
        if q == "SAVE":
            y = int(query[1])
            note[y] = cur
        if q == "LOAD":
            z = int(query[1])
            if z not in note:
                cur = 0
            else:
                cur = note[z]
        ans.append(t.tree[cur].value)
    
    print(*ans)




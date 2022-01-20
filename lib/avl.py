class Node:
    def __init__(self,data):
        self.data = data
        self.left:Node = None
        self.right:Node = None


class AVL:
    def __init__(self):
        self.root = None
        pass


    def search(self,data:int,root):
        if data == root.data:
            return True
        elif data > root.data:
            return self.search(data,root.right)
        else:
            return self.search(data,root.left)
    
    def get_height(self,root:Node):
        if root.right == None and root.left == None:
            return 1
        else:
            right_tree_height = self.get_height(root.right)
            left_tree_height = self.get_height(root.left)
            return max(right_tree_height,left_tree_height) + 1
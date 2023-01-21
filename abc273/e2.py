from collections import defaultdict
class A:
    def __init__(self):
        self.__tree: list[TreeNode] = [TreeNode(-1,-1)]
        self.__cur_tail_idx = 0
        self.__notes = defaultdict(int)
    
    def add(self,x):
        self.__tree.append(TreeNode(self.__cur_tail_idx,x))
        self.__cur_tail_idx = len(self.__tree) - 1
    
    def save(self,y):
        self.__notes[y] = self.__cur_tail_idx
    
    def load(self,z):
        self.__cur_tail_idx = self.__notes[z]
    
    def delete(self):
        if self.__cur_tail_idx == 0:
            return
        self.__cur_tail_idx = self.__tree[self.__cur_tail_idx].p
    
    def tail(self):
        return self.__tree[self.__cur_tail_idx].v
    

    

class TreeNode:
    def __init__(self,p,v):
        self.p = p
        self.v = v

Q = int(input())

X = list()
a = A()
for i in range(Q):
    query = input().split()
    q = query[0]

    if q == "ADD":
        x = int(query[1])
        a.add(x)
    
    if q == "DELETE":
        a.delete()
    
    if q == "SAVE":
        y = int(query[1])
        a.save(y)
    
    if q == "LOAD":
        z = int(query[1])
        a.load(z)
    
    X.append(a.tail())

print(*X)


 "wave_notification"
 "wave_mynews"
 "wave_like_dislike"
 "wave_topic_recommend"
 "wave_rss"
 "wave_video"
 "wave_bookmark"
 "wave_follow"
 "product_ithink"
 "product_vdata"
 "read_morning_and_evening_edition"
 "product_story"
 "product_app"
 "product_web"
 "product_viewer"
 "product_voicy"
 "line_account"

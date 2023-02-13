class Node:
    def __init__(self,p,v):
        self.__p = p
        self.__v = v

    @property
    def p(self):
        return self.__p

    @property
    def v(self):
        return self.__v

class A:
    def __init__(self):
        self.__data:list[Node] = [Node(-1,-1)]
        self.__cur_tail_idx = 0
        self.__note:dict[int,int] = {}

    @property
    def tail(self):
        return self.__data[self.__cur_tail_idx].v

    def add(self,x):
        self.__data.append(Node(self.__cur_tail_idx,x))
        self.__cur_tail_idx = len(self.__data) - 1
    
    def delete(self):
        if self.__cur_tail_idx == 0:
            return
        self.__cur_tail_idx = self.__data[self.__cur_tail_idx].p
    
    def save(self,y):
        self.__note[y] = self.__cur_tail_idx
    
    def load(self,z):
        if z not in self.__note:
            self.__cur_tail_idx = 0
        else:
            self.__cur_tail_idx = self.__note[z]

Q = int(input())
a = A()
X = list()
for i in range(Q):
    q = list(input().split())
    if q[0] == "ADD":
        x = int(q[1])
        a.add(x)
    if q[0] == "DELETE":
        a.delete()
    if q[0] == "SAVE":
        y = int(q[1])
        a.save(y)
    if q[0] == "LOAD":
        z = int(q[1])
        a.load(z)
    X.append(a.tail)

print(*X)

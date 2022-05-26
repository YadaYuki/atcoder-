class Bit:
    def __init__(self,n:int):
        self.n = n
        self.__bits = [0]*(n+1)
    
    def add(self,idx:int,val:int): # idxにvalを追加
        i = idx
        while i < self.n+1:
            self.__bits[i] += val # iビット目から親ノードも追加
            i += (i & -i)

    def sum(self,idx:int): # 区間0 ~ idxまでの和
        s = 0
        while idx > 0:
            s += self.__bits[idx]
            idx -= (idx & -idx)
        return s


n,q = map(int,input().split())
rsq = Bit(n+1)
ans = []


for _ in range(q):
    com,x,y = map(int,input().split())
    if com == 0:
        rsq.add(x, y)
    else:
        ans.append(rsq.sum(y) - rsq.sum(x-1))

for i in ans:
    print(i)
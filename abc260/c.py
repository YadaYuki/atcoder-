N,X,Y = map(int,input().split())

def rec(color,level):
    if level == 1:
        return int(color == "b")
    else:
        if color == "r":
            return rec("r",level-1) + X * rec("b",level)
        else:
            return rec("r",level-1) + Y * rec("b",level-1)



print(rec("r",N))
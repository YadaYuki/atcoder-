HA,WA = map(int,input().split())
A = [list(map(int,input().split())) for i in range(HA)]
HB,WB = map(int,input().split())
B = [list(map(int,input().split())) for i in range(HB)]

def bit_cnt(n:int):
    return bin(n).count("1")

def is_same_mat(a,b):
    if len(a) != len(b):
        return False
    if len(a) == 0 and len(b) == 0:
        return True
    if len(a[0]) != len(b[0]):
        return False
    
    for i in range(len(a)):
        for j in range(len(a[0])):
            if b[i][j] != a[i][j]:
                return False
    return True

for h_pattern in range(2**HA):
    for w_pattern in range(2**WA):
        if bit_cnt(h_pattern) != HB or bit_cnt(w_pattern) != WB:
            continue
        A_removed = list()
        for i in range(HA):
            if (h_pattern >> i & 1) == 1:
                row = list()
                for j in range(WA):
                    if (w_pattern >> j & 1) == 1:
                        row.append(A[i][j])
                A_removed.append(row)
        if is_same_mat(A_removed, B):
            print("Yes")
            exit()
        

print("No")
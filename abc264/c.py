HA,WA = map(int,input().split())
A = [list(map(int,input().split())) for i in range(HA)]
HB,WB = map(int,input().split())
B = [list(map(int,input().split())) for i in range(HB)]
h_bin_cnt = len(bin(2**HA-1)[2:])
w_bin_cnt = len(bin(2**WA-1)[2:])
for rh in range(2**HA):
    rh_bin = list(bin(rh)[2:].zfill(h_bin_cnt))
    if rh_bin.count("1") != HB:
        continue
    for rw in range(2**WA):
        rw_bin = list(bin(rw)[2:].zfill(w_bin_cnt))
        if rw_bin.count("1") != WB:
            continue
        A_removed = list()
        for i in range(HA):
            if rh_bin[i] == "0":
                continue
            A_removed.append(list())
            for j in range(WA):
                if rw_bin[j] == "1":
                    A_removed[-1].append(A[i][j])
        ok = True
        for i in range(HB):
            for j in range(WB):
                if A_removed[i][j] != B[i][j]:
                    ok = False
                    break
            if not ok:
                break
        
        if ok:
            print("Yes")
            exit()
            

print("No")
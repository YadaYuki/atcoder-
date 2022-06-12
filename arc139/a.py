def binary(n:int):
    return bin(n)[2:]

def bin_to_dec(binary:str):
    return int(binary, 2)

if __name__ == "__main__":
    N = int(input())
    T = list(map(int, input().split()))
    A = [-1 for _ in range(N)]
    A[0] = bin_to_dec("1" + "0" * T[0])
    for i in range(1, N):
        A_prev_bin = binary(A[i-1])
        if T[i-1] > T[i]: # A[i-1]の右からT[i]桁目が1
            A_ls = list(A_prev_bin)
            A_ls[-T[i]-1] = "1"
            A[i] = bin_to_dec("".join(A_ls))
        elif T[i-1] == T[i]:
            overwrite= False
            for j in range(-(T[i]+1),-(len(A_prev_bin)+1),-1):
                if A_prev_bin[j] == "0":
                    A_ls = list(A_prev_bin)
                    A_ls[j] = "1"
                    A_prev_bin = "".join(A_ls)
                    overwrite = True
                    break
            if not overwrite:
                A_prev_bin = "1" + A_prev_bin
            A[i] = bin_to_dec(A_prev_bin)
            
        else:
            if len(A_prev_bin) <= T[i]:
                A_bin = "1" + "0" * T[i]
                A[i] = bin_to_dec(A_bin)
            else:
                pass

    print(A)
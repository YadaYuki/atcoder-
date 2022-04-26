def binary(n:int):
    return bin(n)[2:]

def bin_to_dec(binary:str):
    return int(binary, 2)

if __name__ == "__main__":
    N = int(input())
    T = list(map(int, input().split()))
    A_i = list(binary(bin_to_dec("1" + "0" * T[0])))
    A_i.reverse()
    for i in range(1, N):
        if T[i-1] > T[i]:
            A_i[T[i]] = "1"
        elif T[i-1] == T[i]:
            overwrite = False
            for j in range(T[i], len(A_i)):
                if A_i[j] == "0":
                    A_i[j] = "1"
                    overwrite = True
                    break
            if not overwrite:
                A_i.append("1")
        else:
            if len(A_i) <= T[i]:
                A_i.append("0")
            else:
                overwrite_index = -1
                A_i = A_i[:len(A_i)-T[i]] + ["0"] * T[i]
                for j in range(len(A_i)-T[i]):
                    if A_i[j] == "0":
                        overwrite_index = j
                if overwrite_index == -1:
                    A_i = ["1"] + ["0"] * (len(A_i)-T[i]-1) + ["1"] + ["0"] * T[i]
                else:
                    A_i[overwrite_index] = "1"
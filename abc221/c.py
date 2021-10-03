N_str = input()
N = int(N_str)
split_pattern_num = 1 << len(N_str)

def split_N(N_str,binary):
    A,B = [],[]
    for i in range(len(binary)):
        if binary[i] == "0":
            A.append(int(N_str[i]))
        elif binary[i] == "1":
            B.append(int(N_str[i]))
    return A,B

def to_binary(num,length):
    return bin(num)[2:].zfill(length)

ans = 0
for i in range(1,split_pattern_num-1):
    A,B = split_N(N_str,binary=to_binary(i,len(N_str)))
    A.sort(reverse=True)
    B.sort(reverse=True)
    ans = max(ans,int("".join(map(str,A))) * int("".join(map(str,B))))
    
print(ans)




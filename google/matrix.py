

def solve (N, M, K, matrix):
    # Type your code here
    binary_dict = {}

    for i in range(N):
        binary = "".join(list(map(str,matrix[i])))
        if binary_dict.get(binary) is None:
            binary_dict[binary] = 1
        else:
            binary_dict[binary] += 1
    
    ans = -1
    keys = binary_dict.keys()
    # print(binary_dict)
    for binary in keys:
        inverted_binary = "".join(list(map(str,map(lambda x: 1 if x == 0 else 0, list(map(int,list(binary)))))))
        
        if inverted_binary in binary_dict:
            ans = max(ans, binary_dict[binary] + min(K,binary_dict[inverted_binary]))
        else:
            ans = max(ans, binary_dict[binary])
            
    
    return ans
    

    

T = int(input())
ans = []
for _ in range(T):
    N, M, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for i in range(N)]

    out_ = solve(N, M, K, matrix)
    ans.append(out_)
    print (out_)

print(ans)

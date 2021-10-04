N = int(input())
S = input()
W_num_in_west = [0]
for i in range(N):
    if S[N-i-1] == "W":
        W_num_in_west.append(W_num_in_west[i] + 1)
    else:
        W_num_in_west.append(W_num_in_west[i])
W_num_in_west.reverse()

E_num_in_east = [0]

for i in range(N):
    if S[i] == "E":
        E_num_in_east.append(E_num_in_east[i] + 1)
    else:
        E_num_in_east.append(E_num_in_east[i])

ans = float("inf")

print(E_num_in_east)
print(W_num_in_west)
for i in range(N):
    
    ans = min(ans,W_num_in_west[i+1] + E_num_in_east[i])

print(ans)
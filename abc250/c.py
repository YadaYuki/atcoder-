N,Q = map(int,input().split())
x = []

for _ in range(Q):
    x.append(int(input()))

# 右隣の要素と左端かどうかを格納する
right_next_dict = {}
right_next_dict[1] = [2,True]
for i in range(2,N):
    right_next_dict[i] = [i+1,False]
right_next_dict[N] = [1,False]
# print(right_next_dict)
for xi in x:
    right_next_xi,is_left_xi = right_next_dict[xi]
    right_next_xi_right_next_xi,is_left_right_next_xi = right_next_dict[right_next_xi]
    right_next_dict[xi] = [right_next_xi_right_next_xi,is_left_right_next_xi]
    right_next_dict[right_next_xi] = [xi,is_left_xi]

left_item = -1
for key,item in right_next_dict.items():
    if item[1]:
        left_item = key
        break
# a = []
# for 

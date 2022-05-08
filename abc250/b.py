N,A,B = map(int,input().split())


WHITE = "."
BLACK = "#"
# def get_tile_str(A,B,fill=WHITE):
#     s = fill * B
#     s = "\n".join([s] * A)
#     return s

tiles = [[] for _ in range(N)]
ans = ""
for i in range(N):
    left_white_flag = i % 2 == 0
    white_flag = left_white_flag
    s = "" # i行目の文字列
    for j in range(N):
        fill = WHITE if white_flag else BLACK
        s += fill * B
        white_flag = not white_flag
    s = "\n".join([s] * A)
    print(s)


# for i in range(N):
#     left_white_flag = i % 2 == 0
#     white_flag = left_white_flag
#     for j in range(N):
#         if white_flag:
#             tiles[i].append(get_tile_str(A, B, WHITE))
#         else:
#             tiles[i].append(get_tile_str(A, B, BLACK))
#         white_flag = not white_flag

# for i in range(N):
#     for j in range(N):
#         if j != N-1:
#             print(tiles[i][j])
#         if j == N - 1:
#             print(tiles[i][j], end="")
#     # break

# print(ans)

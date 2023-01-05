R,C = map(int,input().split())

# create GRID
GRID_SIZE = 15
GRID = [["black" for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]

white_left_up_ls = [[1,1],[3,3],[5,5],[7,7]]

for white_left_up in white_left_up_ls:
    i,j = white_left_up
    # left up to right up
    for jj in range(j,GRID_SIZE-j):
        GRID[i][jj] = "white"
    
    # left down to right down
    for jj in range(j,GRID_SIZE-j):
        GRID[GRID_SIZE-i-1][jj] = "white"
    
    # left up to left down
    for ii in range(i,GRID_SIZE-i):
        GRID[ii][j] = "white"

    # right up to right down
    for ii in range(i,GRID_SIZE-i):
        GRID[ii][GRID_SIZE-j-1] = "white"

print(GRID[R-1][C-1])



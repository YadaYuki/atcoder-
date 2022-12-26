# create cells
R,C = map(int,input().split())
cells = [["white" for i in range(15)] for j in range(15)]

# fill black

for black in [0,2,4,6]:
    for i in range(black,15-black):
        cells[black][i] = "black"
    for i in range(black,15-black):
        cells[15-black-1][i] = "black"
    for i in range(black,15-black):
        cells[i][black] = "black"
    for i in range(black,15-black):
        cells[i][15-black-1] = "black"

print(cells[R-1][C-1])
x1,y1,x2,y2 = map(int,input().split())

def get_dots_related(coordinate):
    x,y = coordinate
    return [
        (x+1,y+2),
        (x+2,y+1),
        (x-1,y+2),
        (x-2,y+1),
        (x-1,y-2),
        (x-2,y-1),
        (x+1,y-2),
        (x+2,y-1),
    ]

dots_related_1,dots_related_2 = get_dots_related((x1,y1)),get_dots_related((x2,y2))
# print(dots_related_1,dots_related_2)
for dot_related_1 in dots_related_1:
    if dot_related_1 in dots_related_2:
        print('Yes')
        exit()


print('No')
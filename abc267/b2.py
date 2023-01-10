pins = [[6],[3],[1,7],[0,4],[2,8],[5],[9]]
standing_pins = [list() for i in range(7)]
s = list(input())
if s[0] == "1":
    print("No")
    exit()

for i,col in enumerate(pins):
    for p in col:
        if s[p] == "1":
            standing_pins[i].append(p)

for l in range(len(pins)-2):
    if len(standing_pins[l]) == 0:
        continue
    for r in range(l+2,len(pins)):
        if len(standing_pins[r]) == 0:
            continue
        for col_between_l_r in range(l+1,r):
            if len(standing_pins[col_between_l_r]) == 0:
                print("Yes")
                exit()
print("No")
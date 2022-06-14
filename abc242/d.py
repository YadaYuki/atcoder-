S = input()
print(S)
for i in range(3):
    for c,s in [["A","BC"],["B","CA"],["C","AB"]]:
        S = S.replace(c,s)
        print(S)
        



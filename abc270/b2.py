X,Y,Z = map(int,input().split())
S = 0
positions = sorted([S,X,Y,Z])
pos_to_label = {S:"S",X:"X",Y:"Y",Z:"Z"}
position_labels = "".join([pos_to_label[p] for p in positions])
if position_labels.startswith("SY") or position_labels.endswith("YS"):
    print(-1)
    exit()
if position_labels == "ZSYX" or position_labels == "XYSZ":
    print(abs(Z) * 2 + abs(X))
    exit()

print(abs(X))





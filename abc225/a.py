S = input()

c_dict = {}
for c in S:
    c_dict[c] = True


word_num = len(c_dict)
if word_num == 1:
    print(1)
elif word_num == 2:
    print(3)
else:
    print(6)

pencil_dict = {
    'H':False,'2B':False,'3B':False , 'HR':False
}

for _ in range(4):
    S = input()
    pencil_dict[S] = True

for k,v in pencil_dict.items():
    if not v:
        print('No')
        exit(0)

print('Yes')
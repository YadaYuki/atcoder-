a,b,c = list(input())
abc = int(f'{a}{b}{c}')
bca = int(f'{b}{c}{a}')
cab = int(f'{c}{a}{b}')

print(abc+bca+cab)
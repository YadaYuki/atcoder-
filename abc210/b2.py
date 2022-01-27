AOKI,TAKAHASHI = 'Aoki','Takahashi'

N = int(input())
S = input()



for i,card in enumerate(S):
    if card == '1':
        if i%2 == 1:
            print(AOKI)
        else:
            print(TAKAHASHI)
        break


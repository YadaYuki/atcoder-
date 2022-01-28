N = int(input())
A = list(map(int, input().split()))
card_num_in_A = [0] * (N + 1)

for i in range(len(A)):
    card_num_in_A[A[i]] += 1

ans = 0
for i,card_num in enumerate(card_num_in_A):
    if card_num == 3:
        print(i)
        exit()



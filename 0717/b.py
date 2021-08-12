N = int(input())
S = input()
i = 0
BAD_CARD, GOOD_CARD = "1", "0"
for i in range(N):
    if S[i] == BAD_CARD:
        break

if i % 2 == 0:
  print("Takahashi")
else:
  print("Aoki")

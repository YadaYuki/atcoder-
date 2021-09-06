contenst = {"ABC": True,
            "ARC": True,
            "AGC": True,
            "AHC": True}
S1 = input()
S2 = input()
S3 = input()
for s in [S1,S2,S3]:
  contenst[s] = False


for s in contenst:
  if contenst[s] == True:
    print(s)


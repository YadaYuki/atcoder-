# get Arithmetics
def get_arithmetics():
    arithmetics = set()
    for i in range(1,10):
        for diff in range(-9,9):
            s = ""
            d = i
            for digit in range(18):
                s += str(d)
                arithmetics.add(int(s))
                d += diff
                if d < 0 or d > 9:
                    break
    return list(arithmetics)

arithmetics = sorted(get_arithmetics())
X = int(input())
for i in arithmetics:
    if i >= X:
        print(i)
        break
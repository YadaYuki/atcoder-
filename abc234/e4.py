def get_arithmetic(first,diff,n_digits):
    cur = first
    arithmetic_str = ""
    for i in range(n_digits):
        if cur < 0 or cur > 9:
            return None
        arithmetic_str += str(cur)
        cur += diff
    return arithmetic_str
X = int(input())
arithmetics = set()
for first in  range(1,10):
    for diff in range(-9,9):
        for n_digits in range(1,19):
            arithmetic = get_arithmetic(first,diff,n_digits)
            if arithmetic is None:
                continue
            arithmetics.add(int(arithmetic))
arithmetics = sorted(list(arithmetics))

for arithmetic in arithmetics:
    if arithmetic >= X:
        print(arithmetic)
        exit()


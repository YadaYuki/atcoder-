

def get_arithmetics(head,diff,max_digit):
    if head + diff > 9 or head + diff < 0:
        return []
    else:
        arithmetic_arr = [head]
        tail = head + diff
        arithmetics = []
        while len(arithmetic_arr) < max_digit and (0 <= tail and tail <= 9):
            arithmetic_arr.append(tail)
            arithmetics.append(arithmetic_arr[:])
            tail += diff
        return arithmetics

aruthmetics = []
for head in range(1,10):
    aruthmetics.append(head)
    for diff in range(-9,9):
        _arithmetics = get_arithmetics(head,diff,18)
        for a in _arithmetics:
            aruthmetics.append(int("".join(list(map(str,a)))))

arithmetics = sorted(aruthmetics)
X = int(input())
for i in arithmetics:
    if i >= X:
        print(i)
        break
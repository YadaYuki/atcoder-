def get_arithmetics(from_n:int,step:int,max_digit:int)->list: 
    """
    The arithmetic sequence:
    """
    result = []
    arithmetic_arr = []
    tail_n = from_n
    while len(arithmetic_arr)+1 <= max_digit and (0 <= tail_n and tail_n <= 9):
        arithmetic_arr.append(tail_n)
        result.append(int("".join(map(str,arithmetic_arr))))
        tail_n += step
    return result


if __name__ == "__main__":
    patterns = set()
    for f in range(1, 10):
        for step in range(-9, 9):
            ar = get_arithmetics(f, step,18)
            for a in ar:
                patterns.add(a)

    X = int(input())
    patterns = sorted(list(patterns))

    for p in patterns:
        if p >= X:
            print(p)
            break
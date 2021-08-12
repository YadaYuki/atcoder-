import sys
import math
import numpy as np


def calculate_log_factorial(m):  # log(n!) = log(n) + log(n-1) + ... log(2)
    log_factorial = 0.0
    for i in range(2, m+1):
        log_factorial += np.log(i)
    return log_factorial


def get_bigger_label(n: int, m: int) -> str:
    log_factorial = 0.0
    if m > 10**8:
        log_factorial = m * np.log(m) - m
    else:
        log_factorial = calculate_log_factorial(m)
    return "Exponential" if log_factorial < n * np.log(2) else "Factorial"

def main(args):
    n, m = [int(item) for item in args]
    print(get_bigger_label(n, m))

if __name__ == "__main__":
    main(["3", "3"])
    main(["12", "7"])
    main(["381015", "370088033"])
    main(["9999999999", "370088029"])

import math
if __name__ == "__main__":
    X = int(input())
    n = 1
    I_RATE = 1.01
    money = 100
    while True:
        money = int((money * I_RATE))
        if money >= X:
            break
        n += 1
    print(n)


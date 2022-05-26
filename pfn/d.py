# 1~5のサイコロの数に対して、横軸をサイコロの目(結果)とした累積分布関数

import sys
import math
import statistics


def comb(n,c):
   return math.factorial(n)/(math.factorial(n-c) * math.factorial(3))

def f(x,n):
  return x ** n

def get_distribution(dice_cnt):
    distribution = []
    X = list(range(1,100))
    for x in X:
      distribution.append(f(0.01*x,dice_cnt))

    return distribution

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    m = list(map(int,lines[0].split()))
    m_mean = statistics.mean(m)
    ans = -1
    diff = 10**10
    for dice in range(1,6):
        distribution = get_distribution(dice)
        num = -1
        for i in range(1,100):
          if distribution[i-1] > 0.5:
            num = i
            break
        if diff > abs(num-m_mean):
            diff = abs(num-m_mean)
            ans = dice
    print(ans)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)

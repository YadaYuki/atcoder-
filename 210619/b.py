
def main(N:int):
  i = 1
  while i ** 2 + i < 2 * N:
    i += 1
  print(i)


if __name__=='__main__':
  N = int(input())
  main(N)
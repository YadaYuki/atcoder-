if __name__=='__main__':
  N = int(input())
  p = int(N * 1.08)
  if p < 206:
    print("Yay!")
  elif p == 206:
    print("so-so")
  else:
    print(":(")
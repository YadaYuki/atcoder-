
def main(x,y):
  if x == y:
    print(x)
  else:
    a = [x,y]
    if not (0 in a):
      print(0)
    elif not (1 in a):
      print(1)
    elif not (2 in a):
      print(2)

if __name__=='__main__':
  x,y = map(int,input().split())
  main(x,y)

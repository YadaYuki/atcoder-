
def main(X:str):
  # all digits are same or not.
  is_same_digits = len(set((X))) == 1
  # next num
  digits_arr = [int(c) for c in X]
  is_count_up = True
  for i in range(3):
    if  digits_arr[i] + 1 != digits_arr[i+1] and not (digits_arr[i] == 9 and digits_arr[i+1] == 0):
      is_count_up = False

  print("Weak" if (is_count_up or is_same_digits) else "Strong")


if __name__=='__main__':
  X = input()
  main(X)


if __name__=="__main__":
  # coin arr
  coin_arr = [1]
  for i in range(1,10):
    coin_arr.append(coin_arr[i-1] * (i+1))
  
  P = int(input())
  coin_num = 0
  for i in range(9,-1,-1):
    coin_num += int(P / coin_arr[i])
    P = P % coin_arr[i]
  print(coin_num)



if __name__ == "__main__":
  N,K = map(int,input().split())
  c = list(map(int,input().split()))
  candy_dict = {}
  for i in range(K):
    if candy_dict.get(c[i]) == None:
      candy_dict[c[i]] = 1
    else:
      candy_dict[c[i]] += 1
  
  ans = len(candy_dict)
  
  for i in range(1,N-K+1):
    candy_delete,candy_add = c[i-1],c[i+K-1]
    if candy_dict[candy_delete] == 1:
      candy_dict.pop(candy_delete)
    else:
      candy_dict[candy_delete] -= 1
    
    if candy_dict.get(candy_add) == None:
      candy_dict[candy_add] = 1
    else:
      candy_dict[candy_add] += 1
    
    ans = max(ans,len(candy_dict))
  
  print(ans)
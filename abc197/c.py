
def to_binary(num,length):
  return list(bin(num)[2:].zfill(length)) 

def split_array_by_binary(array,binary):
  splited_array = []
  arr = []
  for i in range(len(array)):
    arr.append(array[i])
    if i < len(array) - 1:
      if binary[i] == "1":
        splited_array.append(arr)
        arr = []
  splited_array.append(arr)
  return splited_array

def array_or(array):
  val = 0
  for i in range(len(array)):
    val = val | array[i]
  return val

def array_xor(array):
  val = 0
  for i in range(len(array)):
    val = val ^ array[i]
  return val


N = int(input())
A = list(map(int,input().split()))

ans = float("inf")
for i in range(2 ** (N-1)):
  A_splited= split_array_by_binary(A,to_binary(i,N-1))
  or_val = []
  for i in range(len(A_splited)):
    or_val.append(array_or(A_splited[i]))
  ans = min(ans,array_xor(or_val))

print(ans)
# or_val = []

# for i in range(len(A_splited)):
#   or_val.append(array_or(A_splited[i]))


# print(array_xor(or_val))



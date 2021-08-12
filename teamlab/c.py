# def get_reciprocal_num_sum(n):
#   reciprocal_num_sum = 0.0
#   for i in range(1,n+1):
#     reciprocal_num_sum += 1 / i
#   return reciprocal_num_sum


n = 2
reciprocal_num_sum_arr = [1]
while reciprocal_num_sum_arr[-1] < 15:
  reciprocal_num_sum_arr.append(reciprocal_num_sum_arr[-1] + 1/n)
  n += 1

print(n-1)
# print(reciprocal_num_sum_arr)
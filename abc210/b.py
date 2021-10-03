def get_K_number_system(num_K_str:str,K:int):
    ten_number_system_num = 0
    num_K_str = list(num_K_str)
    num_K_str.reverse()
    for i in range(len(num_K_str)):
        ten_number_system_num += int(num_K_str[i]) * (K ** i)
    
    return ten_number_system_num

K = int(input())
A,B = input().split()

print(get_K_number_system(A,K) * get_K_number_system(B,K))

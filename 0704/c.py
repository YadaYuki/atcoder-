import math

if __name__ == "__main__":
    N, K = [int(item) for item in input().split()]
    a = [int(item) for item in input().split()]
    a_sorted = sorted(a)
    K_dash = K % N
    base_sweets_num = math.floor(K/N)
    sweets_num_arr = [base_sweets_num] * N

    idx_dict = {}

    for i in range(N):
        idx_dict[a[i]] = i

    for i in range(K_dash):
        idx = idx_dict[a_sorted[i]]
        sweets_num_arr[idx] += 1

    for sweets_num in sweets_num_arr:
        print(sweets_num)

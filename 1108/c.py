def get_binary_arr(num,digits_num):
    return [int(item) for item in list(bin(num)[2:].zfill(digits_num))]

if __name__ == "__main__":
    N = input()
    digits_num = len(N)
    N_digit_arr = [int(digit) for digit in N]
    min_delete_digit_num = float("inf")
    for i in range(1,2**digits_num):
        digit_sum = 0
        binary_arr = get_binary_arr(i,digits_num)
        for j in range(digits_num):
            digit_sum += binary_arr[j] * N_digit_arr[j]
        if digit_sum % 3 == 0:
            min_delete_digit_num = min(binary_arr.count(0),min_delete_digit_num)
    if min_delete_digit_num == float("inf"):
        print(-1)
    else:
        print(min_delete_digit_num)


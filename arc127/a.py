N = int(input())

def get_sum_fn(N):
    N_str = str(N)
    if N < 1:
        return 0
    if len(N_str) == 1:
        return 1
    if N_str.startswith('1'):
        digit_by_10 = 10**(len(N_str) - 1)
        a = N-digit_by_10
        digit_by_10_a = 10**(len(str(a)) - 1)
        return (N - digit_by_10 + 1) + get_sum_fn(a) - get_sum_fn(digit_by_10_a-1) + get_sum_fn(digit_by_10-1)
    else:
        fn = 0
        sum_fn = 0
        num_digit = len(N_str) # Nの桁数
        for i in range(num_digit):
            fn = fn + 10 ** i
            sum_fn += fn
        return sum_fn

print(get_sum_fn(N))


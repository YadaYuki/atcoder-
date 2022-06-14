def get_digit_for_k(k):
    """K番目が何桁かを返す"""
    pattern_count_by_n_digit = 0
    digit = 1 # digit桁の0,2で構成される数字は2**(digit-1)個ある
    while pattern_count_by_n_digit + 2**(digit-1) < k:
        pattern_count_by_n_digit += 2**(digit-1)
        digit += 1
    return digit,pattern_count_by_n_digit

def get_ans(K):
    n,pattern_count_by_n_digit = get_digit_for_k(K)
    # n桁の中で何番目かを求める
    digit_k = K- pattern_count_by_n_digit 
    binary = bin(digit_k-1)[2:].zfill(n-1) # 2進数に変換して、0から始まるので2を引く
    return "2" + binary.replace("1", "2")

if __name__ == "__main__":
    K = int(input())
    if K == 1:
        print(2)
        exit()
    # n桁の中で何番目かを求める
    print(get_ans(K))
    
    
    

    



    

    

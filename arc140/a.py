from collections import defaultdict

def get_divisors(n:int):
    divisors = []
    for i in range(1, int(n**0.5+1)):
        if n % i == 0:
            divisors.append(i)
            if i != n//i:
                divisors.append(n//i)
    return divisors

def split_text(text:str, n:int):
    return [text[i:i+n] for i in range(0, len(text), n)]

N,K = map(int, input().split())
S = list(input())
divisors = get_divisors(N)
divisors.sort()
ans = 10**9
for divisor in divisors:
    texts = split_text(S, divisor)
    cost_to_create_iter = 0
    for char_idx in range(divisor):
        # 分割した文字列のchar_idx番目の文字がどのくらい一致しているか
        dict_char_count = defaultdict(int)
        for i in range(len(texts)):
            dict_char_count[texts[i][char_idx]] += 1
        max_count = max(dict_char_count.values())
        cost_to_create_iter += len(texts) - max_count
    if cost_to_create_iter <= K:
        ans = min(ans, divisor)

print(ans)
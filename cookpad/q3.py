import sys

MIN_BLOCK_WEIGHT = 500
ONE_HUDRED_GRAM = 100


def get_max_price(weight: int) -> int:  # solve by DP
    max_price_dict = {}  # {[weight]:max_price,[weight]:max_price,...}
    max_price_dict[MIN_BLOCK_WEIGHT] = get_block_price(MIN_BLOCK_WEIGHT)
    for i in range(1000, weight+MIN_BLOCK_WEIGHT, MIN_BLOCK_WEIGHT):
        price = get_block_price(i)
        for j in range(MIN_BLOCK_WEIGHT, i, MIN_BLOCK_WEIGHT):
            price = max(max_price_dict[j] + max_price_dict[i-j], price)
        max_price_dict[i] = price
    return max_price_dict[weight]


def get_block_price(block_weight_gram: int) -> int:
    if block_weight_gram < 1000:
        return 180 * block_weight_gram / ONE_HUDRED_GRAM

    elif 1000 <= block_weight_gram < 2000:
        return 275 * block_weight_gram / ONE_HUDRED_GRAM

    elif 2000 <= block_weight_gram < 3000:
        block_price = 290 * block_weight_gram / ONE_HUDRED_GRAM
        if block_weight_gram == 2000:
            return block_price * (1-0.2)
        return block_price
    elif 3000 < block_weight_gram:
        return (300 * block_weight_gram / ONE_HUDRED_GRAM) * (1-0.2)


if __name__ == "__main__":
    weight = int(sys.argv[1])
    print(int(get_max_price(weight)))

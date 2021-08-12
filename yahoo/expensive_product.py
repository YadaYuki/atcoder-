
def get_expensive_product_profit_sum(n, k, price_list):
    profit_sum = 0
    for i in range(n):
        price, profit = price_list[i]
        if price >= k:
            profit_sum += profit
    return profit_sum


if __name__ == "__main__":
    n, k = 5, 5000
    price_list = [
    [100, 6135],
    [250, 2935],
    [1000, 4890],
    [5000, 125],
    [10000, 1500],
    ]
    print(get_expensive_product_profit_sum(n,k,price_list))

def maxProfit(prices, fee):
    if len(prices) == 0:
        return 0
    tk0 = 0
    tk1 = -prices[0]

    for price in prices:
        tk0_old = tk0
        tk0 = max(tk0_old, tk1 + price - fee)
        tk1 = max(tk1, tk0_old - price)
        print(tk0, tk1)

    return tk0


prices = [1, 3, 7, 5, 10, 3]
fee = 3
print(maxProfit(prices, fee))

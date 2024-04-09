def daily_rates(prices):
  if len(prices) < 2:
    return []
  
  return [(prices[i+1] - prices[i]) / prices[i] for i in range(len(prices) - 1)]



def daily_prices(start_price, daily_rates):
  prices = [start_price]
  for rate in daily_rates:
    next_price = prices[-1] * (1 + rate)
    prices.append(next_price)

  return prices

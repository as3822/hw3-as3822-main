#Problem 3.1
def daily_returns(prices):
  if len(prices) < 2:
    return []
  
  return [(prices[i+1] - prices[i]) / prices[i] for i in range(len(prices) - 1)]


#Problem 3.2
def daily_prices(start_price, daily_returns):
  prices = [start_price]
  for rate in daily_returns:
    next_price = prices[-1] * (1 + rate)
    prices.append(next_price)

  return prices

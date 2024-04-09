#Problem 1.1
def product(numbers):
  result = 1
  for i in range(len(numbers)):
    result *= numbers[i]

  return result

#Problem 2.1
def cumsum(numbers): 
  cumulative_sums = []

  for i in range(len(numbers)):
    if i == 0:
      cumulative_sums.append(numbers[0])
    else:
      cumulative_sums.append(cumulative_sums[i-1] + numbers[i])
  return cumulative_sums

#Problem 4
def is_increasing(numbers):
  if len(numbers) < 2:
    return True 
  for i in range(1, len(numbers)):
    if numbers[i-1] >= numbers[i]:
      return False
  return True
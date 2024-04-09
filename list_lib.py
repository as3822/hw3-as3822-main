def product(numbers):
  result = 1

  if not numbers:
    return result
  result_type = int
  for num in numbers:
    result *= num
    if isinstance(num, float):
      result_type = float

  return result_type(result)


def cumsum(numbers): 
  cumulative_sums = []

  for i, num in enumerate(numbers):
    if i == 0:
      cumulative_sums.append(num)
    else:
      cumulative_sums.append(cumulative_sums[i-1] + num)
  return cumulative_sums


def is_increasing(numbers):
  if len(numbers) < 2:
    return True 
  for i in range(1, len(numbers)):
    if numbers[i-1] >= numbers[i]:
      return False
  return True

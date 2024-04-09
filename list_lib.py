#Problem 1.1
def product(numbers):
  result = 1
  for i in range(len(numbers)):
    result *= numbers[i]

  return result

#Problem 2.1
def cumsum(nums): 
  sums = []

  for i in range(len(nums)):
    if i == 0:
      sums.append(nums[0])
    else:
      sums.append(sums[i-1] + nums[i])
  return sums

#Problem 4
def is_increasing(numbers):
  if len(numbers) < 2:
    return True 
  for i in range(1, len(numbers)):
    if numbers[i-1] >= numbers[i]:
      return False
  return True
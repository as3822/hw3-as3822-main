from list_lib import product, cumsum

#Problem 1.2
def geometric_mean(numbers):
  for i in range(len(numbers)):
    geometric = product(numbers)
  return geometric ** (1/len(numbers))


#Problem 2.2
def running_mean(nums):
  means = []
  for i in range(len(cumsum(nums))):
    means.append(float((cumsum(nums))[i] / (i+1)))
  return means

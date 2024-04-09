from list_lib import product

#Problem 1.2
def geometric_mean(numbers):
  for i in range(len(numbers)):
    geometric = product(numbers)
  return geometric ** (1/len(numbers))


#Problem 2.2
def running_means(numbers):
  means = []
  for i, num in range(len(numbers)):
    means.append(sum(numbers[:i+1]) / (i+1))
  return means

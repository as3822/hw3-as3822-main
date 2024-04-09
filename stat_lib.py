from list_lib import product

def geometric_mean(numbers):
    #product of all numbers
    product_of_numbers = product(numbers)
    #geometric mean
    geometric_mean = product_of_numbers ** (1 / len(numbers))
    return float(geometric_mean)


#Problem 
def running_means(arr):
  means = []
  for i, num in range(len(arr)):
    means.append(sum(arr[:i+1]) / (i+1))
  return means


# ###    MEAN

# import numbers


# def my_mean(sample):
     
#      average = sum(sample) / len(sample)
     
#      return average

# my_mean()







# ## MEDIAN

# def my_median(sample):
#      n = len(sample)
#      index = n // 2
#      # Sample with an odd number of observations
#      if n % 2:
#          return sorted(sample)[index]
#     # Sample with an even number of observations
#      return sum(sorted(sample)[index - 1:index + 1]) / 2





# ## VARIANCE
# def variance(data):
#      # Number of observations
#      n = len(data)
#      # Mean of the data
#      mean = sum(data) / n
#      # Square deviations
#      deviations = [(x - mean) ** 2 for x in data]
#      # Variance
#      variance = sum(deviations) / n
#      return variance


# import math
# ## STANDARD DEVIATION
# def stdev(data):
#      var = variance(data)
#      std_dev = math.sqrt(var)
#      return std_dev




# ### SKEWNESS
# def skew(n):
#      mean= average(numbers)
#      s=[]
#      for a in numbers:
#           a-=mean
#           a=a**3
#           s.append(a)
#      b=sum(s)
#      try:
#           x=standard_deviation(numbers)
#           v=b/(((numbers_of_numbers)-1)*((x)**3))
#      except Exception:
#           print('No skew found')

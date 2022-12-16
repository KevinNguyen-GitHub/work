# import matplotlib.pyplot as plt
# import numpy as np

# # Read in the data from the CSV file
# csv_file = 'Sales_01_20.csv'
# data = np.loadtxt(csv_file, delimiter = ',', skiprows = 1)
        
# # calculate the mean
# def mean(numbers):
#     """Calculate the mean of an array of numbers"""
#     return sum(numbers) / len(numbers)

# # calculate the std
# def std(numbers):
#     """Calculate the standard deviation of an array of numbers"""
#     mean = mean(numbers)
#     variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
#     return variance ** 0.5

# # Calculate the mean and standard deviation for each year
# yearly_mean = []
# yearly_std = []
# for year in range(2001, 2021):
#     year_data = [x for x in data if x >= year and x < year+1]
#     mean = mean(year_data)
#     std = std(year_data)
#     yearly_mean.append(mean)
#     yearly_std.append(std)

# # Calculate the probability of sale prices within a certain range
# lower_bound = 200000
# upper_bound = 300000
# yearly_probability = []
# for year in range(2001, 2021):
#     year_data = [x for x in data if x >= year and x < year+1]
#     num_within_range = len([x for x in year_data if lower_bound <= x <= upper_bound])
#     probability = num_within_range / len(year_data)
#     yearly_probability.append(probability)

# # Plot the mean values
# plt.hist(data, ec = 'blue')
# plt.title('Yearly Mean Sale Prices')
# plt.xlabel('Year')
# plt.ylabel('Mean Sale Price')
# plt.show()

# # Plot the standard deviation values
# plt.hist(data, ec = 'blue')
# plt.title('Yearly Standard Deviation of Sale Prices')
# plt.xlabel('Year')
# plt.ylabel('Standard Deviation')
# plt.show()

# # Plot the probability values
# plt.hist(data, ec = 'blue')
# plt.title('Yearly Probability of Sale Prices Within a Certain Range')
# plt.xlabel('Year')
# plt.ylabel('Probability')
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Read in the data from the CSV file
csv_file = 'Sales_01_20.csv'
data = np.loadtxt(csv_file, delimiter = ',', skiprows = 1)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

quickSort(data)

# Separate the data into 20 years of data
years = 20
data_by_year = np.array_split(data, years)

# Calculate the mean and standard deviation of sale prices for each year
means = []
stds = []
probabilities = []
for year in data_by_year:
    means.append(np.mean(year))
    stds.append(np.std(year))

# Calculate the probability of sale prices within a certain range
lower_bound = 200000
upper_bound = 300000
probability = np.mean(np.logical_and(year >= lower_bound, year <= upper_bound))
probabilities.append(probability)

# Plot the mean values as a bar graph
fig1, ax1 = plt.subplots()
ax1.bar(range(1, years + 1), means)
ax1.set_title('Yearly Mean Sale Prices')
ax1.set_xlabel('Years')
ax1.set_ylabel('Mean Price')

# Plot the standard deviation values as a bar graph
fig2, ax2 = plt.subplots()
ax2.bar(range(1, years + 1), stds)
ax2.set_title('Yearly Standard Deviation of Sale Prices')
ax2.set_xlabel('Years')
ax2.set_ylabel('Standard Deviation')

# Plot the probability values as a bar graph
fig3, ax3 = plt.subplots()
ax3.bar(range(1, years + 1), probabilities)
ax3.set_title('Yearly Probability of Sale Prices Within a Certain Range')
ax3.set_xlabel('Years')
ax3.set_ylabel('Probability')
plt.show()

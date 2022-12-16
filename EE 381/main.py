import matplotlib.pyplot as plt
import numpy as np

# Read in the data from the CSV file
csv_file = 'Sales_01_20.csv'
data = np.loadtxt(csv_file, delimiter = ',', skiprows = 1)
        
# calculate the mean
def mean(numbers):
    """Calculate the mean of an array of numbers"""
    return sum(numbers) / len(numbers)

# calculate the std
def std(numbers):
    """Calculate the standard deviation of an array of numbers"""
    mean = mean(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance ** 0.5

# Calculate the mean and standard deviation for each year
yearly_mean = []
yearly_std = []
for year in range(2001, 2021):
    year_data = [x for x in data if x >= year and x < year+1]
    mean = mean(year_data)
    std = std(year_data)
    yearly_mean.append(mean)
    yearly_std.append(std)

# Calculate the probability of sale prices within a certain range
lower_bound = 200000
upper_bound = 300000
yearly_probability = []
for year in range(2001, 2021):
    year_data = [x for x in data if x >= year and x < year+1]
    num_within_range = len([x for x in year_data if lower_bound <= x <= upper_bound])
    probability = num_within_range / len(year_data)
    yearly_probability.append(probability)

# Plot the mean values
plt.hist(data, ec = 'blue')
plt.title('Yearly Mean Sale Prices')
plt.xlabel('Year')
plt.ylabel('Mean Sale Price')
plt.show()

# Plot the standard deviation values
plt.hist(data, ec = 'blue')
plt.title('Yearly Standard Deviation of Sale Prices')
plt.xlabel('Year')
plt.ylabel('Standard Deviation')
plt.show()

# Plot the probability values
plt.hist(data, ec = 'blue')
plt.title('Yearly Probability of Sale Prices Within a Certain Range')
plt.xlabel('Year')
plt.ylabel('Probability')
plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Read in the data from the CSV file
csv_file = 'Sales_01_20.csv'
data = np.loadtxt(csv_file, delimiter = ',', skiprows = 1)

# Calculate the mean and standard deviation of the entire dataset
mean = np.mean(data)
std = np.std(data)

# Calculate the probability of sale prices within a certain range
lower_bound = 200000
upper_bound = 300000
probability = np.mean(np.logical_and(data >= lower_bound, data <= upper_bound))

# Plot the mean, standard deviation, and probability values using separate histograms
fig, ax = plt.subplots(3, sharex=True)

ax[0].hist(data, ec='black', alpha=0.5)
ax[0].axvline(mean, color='blue')
ax[0].set_title('Yearly Mean Sale Prices')

ax[1].hist(data, ec='black', alpha=0.5)
ax[1].axvline(std, color='blue')
ax[1].set_title('Yearly Standard Deviation of Sale Prices')

ax[2].hist(data, ec='black', alpha=0.5)
ax[2].axvline(probability, color='blue')
ax[2].set_title('Yearly Probability of Sale Prices Within a Certain Range')

plt.show()
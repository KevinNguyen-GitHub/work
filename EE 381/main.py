import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import sqrt

# Load the dataset from the CSV file
df = pd.read_csv('Sales_01_20.csv')


# Calculate mean
def get_mean(array):
    return sum(array) / len(array)


# Calculate Std
def get_std(array):
    mean_value = sum(array) / len(array)
    variance = sum((x - mean_value) ** 2 for x in array) / (len(array) - 1)
    stdev = sqrt(variance)
    return stdev


# Calculate the mean and standard deviation of sale prices for each year
years = np.unique(df['Year'])
means = []
stds = []
for year in years:
    sale_prices_year = df[df['Year'] == year]['Sale Amount']
    mean = get_mean(sale_prices_year)
    std = get_std(sale_prices_year)
    means.append(mean)
    stds.append(std)

# Show the mean plot
print('2001:', means[0])
print('2005:', means[4])
print('2010:', means[9])
print('2015:', means[14])
print('2020:', means[19], '\n')

plt.bar(years, means)
plt.title('Yearly Mean Sale Prices')
plt.xlabel('Year')
plt.ylabel('Mean')
plt.xticks(np.arange(2000, 2021, 5))
# Show the plot
plt.show()

# Show the standard deviation plot
print('2001:', stds[0])
print('2005:', stds[4])
print('2010:', stds[9])
print('2015:', stds[14])
print('2020:', stds[19], '\n')

plt.bar(years, stds)
plt.title('Yearly Standard Deviation of Sale Prices')
plt.xlabel('Year')
plt.ylabel('STD')
plt.xticks(np.arange(2000, 2021, 5))
# Show the plot
plt.show()

# Calculate the yearly probability of sale price ranging from $200,000 to $300,000
probabilities = []
for year in years:
    sale_prices_year = df[df['Year'] == year]['Sale Amount']
    num_in_range = np.sum((sale_prices_year >= 200000) & (sale_prices_year <= 300000))
    total = len(sale_prices_year)
    probability = num_in_range / total
    probabilities.append(probability)

# Create a plot for probabilities
print('2001:', probabilities[0])
print('2005:', probabilities[4])
print('2010:', probabilities[9])
print('2015:', probabilities[14])
print('2020:', probabilities[19], '\n')

plt.bar(years, probabilities)
plt.title('Yearly Probability of Sale Price Being in Range $200,000-$300,000')
plt.xlabel('Year')
plt.ylabel('Probabilities')
plt.xticks(np.arange(2000, 2021, 5))
# Show the plot
plt.show()

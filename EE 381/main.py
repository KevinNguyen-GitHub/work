import csv
import statistics

# Read in the data from the CSV file
data = []
with open('Sales_01_20.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        data.append(float(row[0]))

# Calculate the mean and standard deviation for each year
yearly_mean = []
yearly_std = []
for year in range(2001, 2021):
    year_data = [x for x in data if x >= year and x < year+1]
    mean = statistics.mean(year_data)
    std = statistics.stdev(year_data)
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

# Plot the results using bar graphs (you will need to use a library like matplotlib for this)
import matplotlib.pyplot as plt

# Plot the mean values
plt.bar(range(2001, 2021), yearly_mean)
plt.title('Yearly Mean Sale Prices')
plt.xlabel('Year')
plt.ylabel('Mean Sale Price')
plt.show()

# Plot the standard deviation values
plt.bar(range(2001, 2021), yearly_std)
plt.title('Yearly Standard Deviation of Sale Prices')
plt.xlabel('Year')
plt.ylabel('Standard Deviation')
plt.show()

# Plot the probability values
plt.bar(range(2001, 2021), yearly_probability)
plt.title('Yearly Probability of Sale Prices Within a Certain Range')
plt.xlabel('Year')
plt.ylabel('Probability')
plt.show()
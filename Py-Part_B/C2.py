# Explore the automobile dataset and visualize the following:

# (i) Distribution of the two and four door cars with respect to the types of fuel they use.

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("automobile_data.csv")

cars = data[['fuel-type', 'num-of-doors']].dropna()
cars = cars[cars['num-of-doors'] != '?']

table = pd.crosstab(cars['num-of-doors'], cars['fuel-type'])

table.plot(kind='bar')

plt.title("Distribution of Two and Four Door Cars by Fuel Type")
plt.xlabel("Number of Doors")
plt.ylabel("Number of Cars")

plt.show()

# (ii) Distribution of cars of different body styles with respect to the type of fuel they use.
#                                           (or)
# (ii) Total number of each type of body style cars categorized by fuel type.

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("automobile_data.csv")

cars = data[['fuel-type', 'body-style']].dropna()

table = pd.crosstab(cars['body-style'], cars['fuel-type'])

table.plot(kind='bar')

plt.title("Distribution of Car Body Styles by Fuel Type")
plt.xlabel("Body Style")
plt.ylabel("Number of Cars")

plt.show()

# (iii) Horsepower of each fuel type with reference to the type of drive wheel present in the car.

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("automobile_data.csv")

cars = data[['fuel-type', 'drive-wheels', 'horsepower']]

cars = cars[cars['horsepower'] != '?']

cars['horsepower'] = pd.to_numeric(cars['horsepower'])

table = pd.pivot_table(
    cars,
    values='horsepower',
    index='fuel-type',
    columns='drive-wheels',
    aggfunc='mean'
)

table.plot(kind='bar')

plt.ylabel("Average Horsepower")

plt.show()

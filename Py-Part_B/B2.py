#Using the data on births in the United States, provided by the Centers for Disease Control (CDC), Find 
# i) Total number of US births by year and gender 

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("births.csv")
year_gender = df.groupby(['year', 'gender'])['births'].sum().unstack()
year_gender.plot()
plt.show()

# ii) Average daily births by day of week and decade

import pandas as pd
import matplotlib.pyplot as plt

# Remove missing values
df = df.dropna(subset=['year', 'month', 'day'])

# Convert to date safely
df['date'] = pd.to_datetime(
    df[['year', 'month', 'day']],
    errors='coerce'
)

df = df.dropna(subset=['date'])
df['weekday'] = df['date'].dt.dayofweek
df['decade'] = (df['year'] // 10) * 10
df.groupby(['weekday', 'decade'])['births'].mean().unstack().plot()
plt.xlabel("Weekday")
plt.ylabel("Average Births")
plt.title("Average Daily Births by Weekday and Decade")
plt.show()
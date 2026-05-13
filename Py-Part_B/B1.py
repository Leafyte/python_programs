# Explore the bicycle counts on Seattle’s Fremont Bridge Data with respect to 
# i) Average daily bicycle counts 
# ii) Average hourly bicycle counts by weekday and weekend.

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("Bridge.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Total bicycles
df['Total'] = df.iloc[:, 2] + df.iloc[:, 3]

# ----------- i) Day-wise average -----------

df['day'] = df['Date'].dt.dayofweek
day_avg = df.groupby('day')['Total'].mean()
day_avg.index = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
day_avg.plot(kind='bar', title='Average Daily Counts')
plt.show()

# ----------- ii) Hourly (Weekday vs Weekend) -----------

df['hour'] = df['Date'].dt.hour
df['type'] = 'Weekday'
df.loc[df['day'] >= 5, 'type'] = 'Weekend'
hour_avg = df.groupby(['hour', 'type'])['Total'].mean().unstack()
hour_avg.plot(title='Hourly (Weekday vs Weekend)')
plt.show()
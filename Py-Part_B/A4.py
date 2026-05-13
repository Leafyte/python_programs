# Read the given data “churn.csv” and save it as a dataframe called churn_data. 
# Perform following operations on the dataframe 

import pandas as pd

# Read CSV file into a dataframe
data = pd.read_csv('churn.csv')

df = pd.DataFrame(data)

# Display the original dataframe
print("Original Data Frame:")
print(df)

# i) Count the number of duplicate records
duplicate_count = df.duplicated().sum()

# Display the count of duplicate records
print("\nNumber of Duplicate Records:", duplicate_count)

# ii) Count the number of duplicate records based on CustomerID
duplicate_count_customer_id = df.duplicated(subset=['customerID']).sum()

# Display the count of duplicate records based on CustomerID
print("\nNumber of duplicate records based on CustomerID column:",duplicate_count_customer_id)

# iii) Count the number of missing values in each column
missing_values_per_column = df.isnull().sum()

# Display the count of missing values in each column
print("\nNumber of Missing Values in Each Column:")
print(missing_values_per_column)

# iv) Count the total number of missing values for TotalCharges
total_missing_values_total_charges = df['TotalCharges'].isnull().sum()

# Display
print("\nTotal number of missing values in TotalCharges:",total_missing_values_total_charges)

# v) Calculate average monthly charge
average_monthly_charge = df['MonthlyCharges'].mean()

print("\nAverage Monthly Charge:",average_monthly_charge)

# vi) Display records where Dependents is "Yes"
filtered_records = df[df['Dependents'] == 'Yes']

print("\nRecords where Dependents is Yes:")
print(filtered_records)

# Replace null values by median value
median_value = df['TotalCharges'].median()

df['TotalCharges_Median_Filled'] = df['TotalCharges'].fillna(median_value)

print("\nNull values replaced using median:")
print(df['TotalCharges_Median_Filled'])

# Replace null values by mode value
max_count_category = df['TotalCharges'].mode().iloc[0]

df['TotalCharges_Mode_Filled'] = df['TotalCharges'].fillna(max_count_category)

print("\nNull values replaced using mode:")
print(df['TotalCharges_Mode_Filled'])
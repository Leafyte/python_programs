# Read the given data “churn.csv” and save it as a dataframe called churn_data. 
# Perform following operations on the dataframe 

import pandas as pd

# Read the CSV file and store it in a dataframe
df = pd.read_csv("churn.csv")

# Display the dataframe
print("Churn Data:")
print(df)

# i) Count total number of duplicate records
total_duplicates = df.duplicated().sum()
print("\n1. Total Number of Duplicate Records:", total_duplicates)

# ii) Count duplicate records based on CustomerID
customerid_duplicates = df.duplicated(subset=["customerID"]).sum()
print("\n2. Number of Duplicate Records based on CustomerID:", customerid_duplicates)

# iii) Count number of missing values in each column
missing_values = df.isnull().sum()
print("\n3. Missing Values in Each Column:")
print(missing_values)

# iv) Count total number of missing values in TotalCharges
missing_totalcharges = df["TotalCharges"].isnull().sum()
print("\n4. Missing Values in TotalCharges:", missing_totalcharges)

# v) Calculate average monthly charge
average_monthly_charge = df["MonthlyCharges"].mean()
print("\n5. Average Monthly Charge:", average_monthly_charge)

# vi) Display records having '1@#' under Dependents
dependents_records = df[df["Dependents"] == "1@#"]
print("\n6. Records having '1@#' in Dependents:")
print(dependents_records)

# vii)Replace null values with Median
df["TotalCharges_Median"] = df["TotalCharges"].fillna(df["TotalCharges"].median())

print("\n7. TotalCharges after replacing null values with Median:")
print(df["TotalCharges_Median"])


# Replace null values with Mode
df["TotalCharges_Mode"] = df["TotalCharges"].fillna(df["TotalCharges"].mode()[0])

print("\n8. TotalCharges after replacing null values with Mode:")
print(df["TotalCharges_Mode"])

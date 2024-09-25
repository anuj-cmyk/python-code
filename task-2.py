import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# loading dataset from PC

df = pd.read_csv("C:\\Users\\anujs\\OneDrive\\python code\\INDIAvi.csv")
print(df)     #for printing the data 

df.head()   # for displaying few data from dataset

summary_stats = df.describe()
print(summary_stats)

# checking the null values 

missing_values = df.isnull().sum()
print("Missing values:\n", missing_values)

# creating histogram 
df.hist(figsize=(10, 10), bins=30)
plt.tight_layout()
plt.show()

# creating box plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, orient="h")
plt.title("Box Plot for Numeric Variables")
plt.show()



# Pairplot for scatter plots across different variables
sns.pairplot(df)
plt.show()


# Calculate the correlation matrix
correlation_matrix = df.corr()

# Display correlation matrix
print(correlation_matrix)

# Visualize correlation matrix using heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Heatmap") 
plt.show()


# Visualize missing values with a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap")
plt.show()


# Drop rows with missing values or fill them using imputation
df_cleaned = df.dropna()  # Remove missing values
 


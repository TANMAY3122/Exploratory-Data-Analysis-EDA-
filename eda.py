# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
# Assuming the dataset is in CSV format
data = pd.read_csv('retail_data.csv')

# Step 1: Data Cleaning and Preprocessing

# Check for missing values
missing_data = data.isnull().sum()

# Fill missing values or drop them
data = data.dropna()  # or you can fill missing values as appropriate

# Convert relevant columns to correct data types
data['Customer_Age'] = data['Customer_Age'].astype(int)
data['Purchase_Amount'] = data['Purchase_Amount'].astype(float)

# Step 2: Exploratory Data Analysis (EDA)

# Descriptive statistics
summary = data.describe()

# Unique values in categorical columns
unique_genders = data['Gender'].unique()
unique_categories = data['Product_Category'].unique()

# Total sales by product category
category_sales = data.groupby('Product_Category')['Purchase_Amount'].sum().sort_values(ascending=False)

# Average purchase amount by age group
data['Age_Group'] = pd.cut(data['Customer_Age'], bins=[18, 25, 35, 50, 65, 100], labels=['18-25', '26-35', '36-50', '51-65', '65+'])
age_group_sales = data.groupby('Age_Group')['Purchase_Amount'].mean()

# Top 10 customers by total spending
top_customers = data.groupby('Customer_ID')['Purchase_Amount'].sum().sort_values(ascending=False).head(10)

# Correlation matrix
corr = data.corr()

# Step 3: Data Visualization

# a. Bar plot for total sales by product category
plt.figure(figsize=(10, 6))
category_sales.plot(kind='bar', color='skyblue')
plt.title('Top 5 Product Categories by Sales')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()

# b. Bar plot for average purchase amount by age group
plt.figure(figsize=(8, 5))
age_group_sales.plot(kind='bar', color='green')
plt.title('Average Purchase Amount by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average Purchase Amount')
plt.show()

# c. Horizontal bar plot for top 10 customers by total spending
plt.figure(figsize=(8, 6))
top_customers.plot(kind='barh', color='purple')
plt.title('Top 10 Customers by Total Spending')
plt.xlabel('Total Spending')
plt.ylabel('Customer ID')
plt.show()

# d. Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Step 4: Draw Insights and Reporting
# These insights will be added in the report below.

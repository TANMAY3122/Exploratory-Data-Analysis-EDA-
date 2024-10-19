# **Customer Segmentation for a Retail Company**
## Exploratory Data Analysis (EDA) Project

### **Project Overview**
This project focuses on performing **Exploratory Data Analysis (EDA)** for a retail company to understand customer behavior and segment customers based on their purchasing patterns. The insights gathered will help the company in improving its sales strategies, targeting high-value customers, and promoting the best-selling products.

The EDA process involves cleaning and preparing the data, visualizing trends, and extracting key insights that will inform actionable business recommendations.

### **Table of Contents**
1. [Project Structure](#project-structure)
2. [Dataset Description](#dataset-description)
3. [EDA Steps](#eda-steps)
4. [Key Findings](#key-findings)
5. [Technologies Used](#technologies-used)
6. [Installation & Setup](#installation-and-setup)
7. [How to Use the Code](#how-to-use-the-code)
8. [Future Improvements](#future-improvements)
9. [Contributing](#contributing)
10. [License](#license)

---

### **Dataset Description**
The dataset used for this project contains retail transaction data, including customer demographics and sales information. It contains the following key features:

- **Customer_ID**: Unique identifier for each customer.
- **Customer_Age**: Age of the customer.
- **Gender**: Gender of the customer.
- **Product_Category**: The category of products purchased.
- **Purchase_Amount**: The amount spent by the customer on each purchase.

---

### **EDA Steps**
Here’s a summary of the steps taken during the EDA process:

1. **Data Cleaning & Preprocessing**: 
   - Identified and handled missing values.
   - Converted columns to appropriate data types (e.g., customer age and purchase amount).
   
2. **Descriptive Statistics**:
   - Calculated basic statistics like mean, median, standard deviation for numeric features.
   - Explored unique values in categorical columns.

3. **Aggregating Data**:
   - Grouped data by product category to calculate total sales.
   - Grouped data by age group to understand average purchasing behavior.
   - Identified top 10 customers by total spending.

4. **Visualizations**:
   - Bar plots for total sales by product category.
   - Bar plots for average purchase amount by age group.
   - Horizontal bar plot for top customers by total spending.
   - Heatmap for correlations between numerical features.

5. **Drawing Insights**:
   - Analyzed trends based on product sales and customer segments.
   - Extracted actionable insights (e.g., top-selling categories, high-value customers, age group behavior).

---

### **Key Findings**
- **Top Product Categories**: Certain product categories contribute to the bulk of sales, suggesting that the company should focus on promoting these categories.
- **High-Value Customers**: A small group of customers contributes to a large portion of the revenue. These customers should be rewarded with loyalty programs or special offers.
- **Age Group Insights**: Customers aged **36-50** are the most valuable in terms of average purchase amount.
- **Gender-Based Insights**: Female customers tend to spend more on average than male customers.
- **Correlations**: Purchase frequency correlates strongly with total spending, indicating that customers who shop more often tend to spend more overall.

---

### **Technologies Used**
- **Programming Language**: Python
- **Libraries**:
  - **Pandas**: For data manipulation and analysis.
  - **Matplotlib/Seaborn**: For creating visualizations.
- **Jupyter Notebooks** (optional): For interactive data analysis.
  
For further reporting or dashboards, tools like **Tableau** or **Power BI** can be used to present the findings in an interactive format.

---

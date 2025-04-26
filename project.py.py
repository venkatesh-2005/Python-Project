import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("E:\\PYTHON PROGRAMS VS\\Candy_Sales.csv")
#
#Objective1: Calculate total and average sales
total_sales = data['Sales'].sum()
average_sales = data['Sales'].mean()
print(f"Total Sales: {total_sales}")
print(f"Average Sales: {average_sales}")

#Objective 2: Analyze sales trends over time
data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Year'] = data['Order Date'].dt.year
sales_trend = data.groupby('Year')['Sales'].sum()

plt.figure(figsize=(10, 6))
plt.plot(sales_trend.index, sales_trend.values, marker='o')
plt.title('Sales Trends Over Time')
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.show()

#Objective 3: Identify top-selling candy products
top_products = data.groupby('Product Name')['Sales'].sum().sort_values(ascending=False)
print("\nTop-Selling Candy Products:")
print(top_products.head())

#Objective 4: Plot distribution of sales
plt.figure(figsize=(10, 6))
sns.histplot(data['Sales'], kde=True)
plt.title('Distribution of Sales')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()

#Objective 5: Visualize regional sales performance
regional_sales = data.groupby('Region')['Sales'].sum()
plt.figure(figsize=(10, 6))
regional_sales.plot(kind='bar')
plt.title('Regional Sales Performance')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.show()

#Objective 6: Examine monthly sales patterns
data['Month'] = data['Order Date'].dt.month
monthly_sales = data.groupby('Month')['Sales'].sum()

plt.figure(figsize=(10, 6))
monthly_sales.plot(marker='o')
plt.title('Monthly Sales Patterns')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()

#Objective 7: Heatmap
numeric_data = data.select_dtypes(include=['number'])
correlation_matrix = numeric_data.corr()

plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Heatmap of Candy Sales Data')
plt.show()

#Objective 8: Pairplot
sns.pairplot(numeric_data)
plt.title('Pairplot of Candy Sales Data')
plt.show()


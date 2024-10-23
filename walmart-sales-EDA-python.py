#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns


# In[5]:


df=pd.read_csv("WalmartSalesData.csv")


# In[6]:


df.head()


# In[28]:


df.info()

#data.shape
df.columns
#data.isna().sum()


# In[8]:


data.describe() #.round()


# ## Business Question To Answer
# 
# ### Generic Question
# 
# 1. How many distinct cities are present in the dataset?
2. 
# In which city is each branch situated?
# 

# In[12]:


#Count the distinct cities in the dataset

distinct_city=df['City'].unique()
#num_distinct_city=df['City'].nunique()
# Print the number of unique cities
print("Distinct cities:", distinct_city)
print("Number of Distinct cities:", len(distinct_city))


# In[26]:


branch_city = df.groupby('City')['Branch'].unique()
#This snippet performs grouping by 'City', and for each city, it extracts the unique 'Branch' values.
branch_city

df.groupby(['City', 'Branch']).unique()
# ## Product Analysis
# 
# 1. How many distinct product lines are there in the dataset?
# 
# 2. What is the most common payment method?
# 
# 3. What is the most selling product line?
# 
# 4. What is the total revenue by month?
# 
# 5. Which month recorded the highest Cost of Goods Sold (COGS)?
# 
# 6. Which product line generated the highest revenue?
# 
# 7. Which city has the highest revenue?
#    
# 8. Which product line incurred the highest VAT?
# 9. Retrieve each product line and add a column product_category, indicating 'Good' or 'Bad,' based on
# 10. Whether its sales are above the average.
# 11. Which branch sold more products than average product sold?
# 12. What is the most common product line by gender?
# 13. What is the average rating of each product line?
# 

# In[32]:


prod_line=df['Product line'].unique()
prod_nline=df['Product line'].nunique()
print("Number of Unique Product Line:",prod_nline)
print("Unique Product Line:",prod_line)


# In[44]:


# What is the most common payment method?
# Count the occurrences of each payment method
payment_counts = df["Payment"].value_counts()

# Get the most common payment method
most_common_payment = payment_counts.idxmax()
n_most_common_payment = payment_counts.max()

# Print the result
print("The most common payment method is:", most_common_payment,"with total of",n_most_common_payment,"times.")

# Plot the payment method frequencies

payment_counts = df["Payment"].value_counts()

plt.bar(payment_counts.index, payment_counts.values)
plt.xlabel("Payment Method")
plt.ylabel("Frequency")
plt.title("Payment Method Frequencies")

# Adjust the y-axis to start from 250
#plt.ylim(300, max(payment_counts.values) + 10)

plt.show()


# In[58]:


# Group the data by product line and calculate the sum of quantities sold
product_line_sales = df.groupby('Product line')['Quantity'].sum()

# Find the product line with the highest quantity sold
most_selling_product_line = product_line_sales.idxmax()

print("The most selling product line is:", most_selling_product_line)

plt.figure(figsize=(10, 6))  # Adjust figure size for better visibility

plt.bar(product_line_sales.sort_values(ascending=True).index, 
               product_line_sales.sort_values(ascending=True).values)

plt.title('Total Quantity Sold by Product Line')
plt.xlabel('Product Line')
plt.ylabel('Total Quantity Sold')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

plt.show()


# In[64]:


# Convert the "Date" column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Extract the month from the "Date" column
df['Month'] = df['Date'].dt.month

# Calculate the total revenue by month
revenue_by_month = df.groupby('Month')['Total'].sum()

print(revenue_by_month)

fig= plt.figure(figsize=(10, 6))
revenue_by_month.plot(kind='bar')
plt.title('Total Revenue by Month')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
#fig.savefig("b.png")
plt.show()


# In[67]:


# Calculate the total revenue by month
large_CGOS_month = df.groupby('Month')['cogs'].sum()

print(large_CGOS_month)

#plot month with highest larget COGS
fig= plt.figure(figsize=(10, 6))
large_CGOS_month.plot(kind='bar')
plt.title('Largest COGS by Month')
plt.xlabel('Month')
plt.ylabel('COGS')
fig.savefig("c.png")
plt.show()


# In[69]:


# Calculate the revenue for each product line
df['Revenue'] = df['Quantity'] * df['Unit price']

# Group the data by product line and calculate the sum of revenue
product_line_revenue = df.groupby('Product line')['Revenue'].sum()

# Find the product line with the largest revenue
largest_revenue_product_line = product_line_revenue.idxmax()

print("The product line with the largest revenue is:", largest_revenue_product_line)

plt.figure(figsize=(10, 6))
product_line_revenue.plot(kind='bar')
plt.title('Total Revenue by Product Line')
plt.xlabel('Product Line')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.show()


# In[70]:


# Calculate the revenue for each product line

df['Revenue'] = df['Quantity'] * df['Unit price']
city_high_revenue = df.groupby('City')['Revenue'].sum()
city_high_revenue_name = city_high_revenue.idxmax()
print("The city with the largest revenue is:", city_high_revenue_name)

plt.figure(figsize=(10, 6))
city_high_revenue.plot(kind='bar')
plt.title('Largest Revenue by City')
plt.xlabel('City')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.show()


# In[71]:


product_line_vat= df.groupby('Product line')['Tax 5%'].sum()

largest_product_line_vat= product_line_vat.idxmax()
print("The product line with the largest VAT is:", largest_product_line_vat)

plt.figure(figsize=(10, 6))
product_line_vat.plot(kind='bar')
plt.title('Largest VAT by product Line')
plt.xlabel('Product Line')
plt.ylabel('VAT')
plt.xticks(rotation=45)
plt.show()


# In[73]:


# Calculate the average sales. 

average_sales = df['Total'].mean()

# Add a new column 'Sales Status' to indicate whether sales are 'Good' or 'Bad'
df['Sales Status'] = df['Total'].apply(lambda x: 'Good' if x > average_sales else 'Bad')

# Display the updated DataFrame
print(df)


# The lambda function allows you to quickly create a simple function in-line (without naming it) to decide whether the sales status should be 'Good' or 'Bad'. This avoids the need to define a separate function with def.
# 
# def sales_status(x):
#     if x > average_sales:
#         return 'Good'
#     else:
#         return 'Bdata['Sales Status'] = data['Total'].apply(sales_status)
# ad'
# 

# In[79]:


# Calculate the average number of products sold
average_products_sold = df['Quantity'].mean()

#********
# Filter the DataFrame to include branches with sales greater than the average
branches_above_average = df[df['Quantity'] > average_products_sold]['Branch'].unique()

print(branches_above_average)

# Display the branches that sold more products than the average
#print("Branches with sales above average:")
#for branch in branches_above_average:
#print(branch)

branches_above_average = df[df['Quantity'] > average_products_sold]['Branch'].value_counts()
plt.bar(branches_above_average.index, branches_above_average.values)
plt.xlabel('Branch')
plt.ylabel('Number of Products Sold')
plt.title('Branches with Sales Above Average')
plt.show()


# In[81]:


grouped_data = df.groupby(['Gender', 'Product line']).size().reset_index(name='Count')
#************

# Find the most common product line for each gender
most_common_product_line = grouped_data.groupby('Gender')['Count'].idxmax()
most_common_product_line_data = grouped_data.loc[most_common_product_line]

# Display the most common product line for each gender
print(most_common_product_line_data[['Gender', 'Product line']])

# Plotting the bar graph
plt.bar(most_common_product_line_data['Gender'], most_common_product_line_data['Count'])
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Most Common Product Line by Gender')
plt.show()


# In[84]:


#What is the average rating of each product line?

avg_rating=df.groupby('Product line')['Rating'].mean()
print(avg_rating)


# In[ ]:





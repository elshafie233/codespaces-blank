import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


sales = pd.read_csv('/workspaces/codespaces-blank/E-commerce Analyzer/Ecommerce_Sales.csv')
products = pd.read_csv('/workspaces/codespaces-blank/E-commerce Analyzer/Ecommerce_Products.csv')


sales = sales.ffill().dropna()


df = sales.merge(products, on='Product_ID')

print("Sales Data Analysis:")
print(df.to_string())


df['Total_Revenue'] = df['Quantity'].to_numpy() * df['Price_Per_Unit'].to_numpy()
print("\nTotal Revenue Calculation:")
print(df[['Transaction_ID', 'Product_ID', 'Quantity', 'Price_Per_Unit', 'Total_Revenue']].to_string())


df['order_type'] = np.where(df['Total_Revenue'] > 100, 'High Value', 'Normal Value')
print("\nOrder Type Classification:")
print(df[['Transaction_ID', 'Total_Revenue', 'order_type']].to_string())


category_revenue = df.groupby('Category')['Total_Revenue'].sum()
print("\nCategory Revenue:")
print(category_revenue)

fig, ax = plt.subplots(figsize=(10, 6))
background_color = '#f0f0f0'
ax.set_facecolor(background_color)

ax.bar(category_revenue.index, category_revenue.values, color='#4682b4', zorder=3)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.5)

ax.set_axisbelow(True) 


ax.bar_label(ax.containers[0], fmt='$%.2f', padding=3, fontsize=10)

plt.title('Total Revenue by Product Category', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Category', fontsize=11, labelpad=10)
plt.ylabel('Total Revenue ($)', fontsize=11, labelpad=10)
plt.tight_layout()

plt.savefig('total_revenue_by_category.png', dpi=300, bbox_inches='tight')
plt.show()

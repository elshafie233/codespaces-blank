# 🛒 E-Commerce Sales & Revenue Analyzer

Hey! This is a clean, straightforward Python workflow I set up to take raw e-commerce transaction data, combine it with product catalog information, and break down revenue performance across different item categories. 

It handles data merging, feature engineering, order classification, and wraps everything up with a polished, presentation-ready bar chart.

---

## 🚀 What the Script Does

* **Cleans & Merges Data:** It reads your sales records and product inventory details, applies a forward-fill (`ffill()`) to handle any missing values, and merges them using the common `Product_ID`.
* **Calculates Financial Metrics:** It converts pandas columns to NumPy arrays to efficiently calculate the `Total_Revenue` for every individual transaction.
* **Segments Orders:** It automatically tags orders based on size. Anything over $100 is classified as a 'High Value' order, while the rest are marked as 'Normal Value'.
* **Aggregates by Category:** It groups the data by product category to calculate exactly how much money each sector is bringing in.
* **Generates a Clean Plot:** It outputs a high-resolution bar chart (`total_revenue_by_category.png`) with styled gray backgrounds, custom gridlines, and floating currency data labels.

---

## 🛠️ Requirements & Workspace Paths

To get this running, make sure you have the standard data stack installed:

```bash
pip install pandas numpy matplotlib
```

### 📂 File Structure Note
The script looks for your CSV files inside a specific Codespaces path:
* `/workspaces/codespaces-blank/E-commerce Analyzer/Ecommerce_Sales.csv`
* `/workspaces/codespaces-blank/E-commerce Analyzer/Ecommerce_Products.csv`

*If you move this project to a local machine or a different directory, remember to update those two `pd.read_csv()` paths at the top of the file so the script can find your data!*

---

## 📊 Reading the Visual Output

When the plot pops up:
* **The Bars:** Represent your overall total revenue per category. 
* **Data Labels:** The script automatically formats the top of each bar with its exact currency value (`$XX.XX`) so you don't have to squint at the Y-axis to guess the numbers.
* **The Export:** A clean copy is saved as `total_revenue_by_category.png` in your root folder with the edges neatly trimmed (`bbox_inches='tight'`) so it's ready to drop straight into a slideshow or report.

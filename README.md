# Retail Inventory and Sales Analysis

## Project Overview

This project analyses retail sales data from a simulated clothing store to understand sales performance and promotional strategies.

The store contains three main zones:
- Men
- Women
- Kids

Each zone includes different product categories such as clothing, accessories, and perfume.

The goal of this project is to use data analysis to explore:
- Which store zones generate the most revenue
- Which product categories contribute the most to total sales
- How promotions are used across different products
- Whether promotions affect the number of units sold

This type of analysis helps retailers make more informed decisions about pricing, product focus, and promotional strategies.

---

# Dataset
The dataset used in this project was generated to simulate a retail store environment.

It contains information about:
- product category
- store zone
- price
- stock level
- units sold
- promotion status
- transaction date

The dataset contains **5000 simulated transactions**.

---

## Tools Used
This project was completed using:

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

These tools were used for data cleaning, analysis, and visualization.

---

# Key Analysis Steps

The project includes several stages of analysis:

### 1. Data Understanding
- Examined dataset structure
- Reviewed data types and summary statistics

### 2. Revenue Analysis
- Calculated revenue using  
  `revenue = price × units_sold`
- Compared revenue across store zones
- Identified the highest revenue product categories

### 3. Promotion Analysis
- Examined how promotions are distributed across product categories
- Compared average units sold with and without promotions
- Analyzed the impact of promotions on sales performance

---

# Key Insights

- **Revenue by store zone:**  
  The Kids and Women zones generate slightly higher total revenue than the Men zone.

- **Top revenue categories:**  
  Footwear and Perfume generate the highest revenue among product categories.

- **Promotion usage:**  
  Promotions are most frequently applied to categories such as Perfume, Footwear, and Accessories.

- **Promotion effectiveness:**  
  Promotions show only small differences in average units sold compared to non-promotional sales.

---

# Business Recommendations

Based on the analysis, several opportunities could be explored:

- **Maintain strong inventory for high-revenue categories**  
  Categories like Footwear and Perfume drive a large portion of store revenue.

- **Evaluate promotional strategy**  
  Since promotions do not significantly increase units sold in this dataset, retailers may need to review how promotions are applied.

- **Support lower-performing product categories**  
  Promotions may be more effective when used to improve sales of weaker categories rather than products that already perform well.

- **Use data-driven decision making**  
  Monitoring category performance and promotion impact can help retailers refine marketing strategies.

---

## Project Structure

This repository is organized as follows:

- **data/**  
  Contains the dataset used in this project.  
  - `retail_sales.csv` – Simulated retail sales dataset used for the analysis.

- **notebooks/**  
  Contains the main analysis notebook.  
  - `retail_sales_analysis.ipynb` – Jupyter Notebook with the full data analysis, visualizations, and insights.

- **README.md**  
  Provides an overview of the project, including objectives, methods, and key insights.

- **LICENSE**  
  Specifies how this project can be used or shared.

- **.gitignore**  
  Lists files and folders that should not be tracked by Git.

---

# References

This project used several learning resources for Python data analysis and visualization:

- GeeksforGeeks – Python data analysis tutorials  
  https://www.geeksforgeeks.org/

- Pandas Documentation  
  https://pandas.pydata.org/docs/

- Seaborn Documentation  
  https://seaborn.pydata.org/

- Matplotlib Documentation  
  https://matplotlib.org/

These resources were used to support implementation of data analysis techniques and visualization methods.

# Task_04_Descriptive_Stats

## Overview

This project performs comprehensive descriptive statistical analysis on multiple real-world datasets centered around the 2024 U.S. presidential election and associated social media activities. The project demonstrates how the same data can be analyzed using three distinct approaches in Python, highlighting differences in code complexity, runtime efficiency, and usability:

- **Pure Python:** Using only the Python Standard Library for maximum transparency and minimal dependencies.  
- **Pandas:** A popular and versatile Python library for data manipulation and analysis.  
- **Polars:** An emerging DataFrame library designed for speed and scalability on large datasets.

By applying these methods to identical datasets, this project showcases how descriptive statistics—including summary statistics, unique counts, frequent values, and group-level aggregations—can be consistently generated across different tools.

---

## Repository Structure

- **pure_python_stats.py**  
  Implements descriptive statistics computation using Python’s built-in modules. Suitable for environments without external libraries.

- **pandas_stats.py**  
  Uses Pandas DataFrames to load and analyze data, utilizing efficient built-in methods like `.describe()`, `.nunique()`, and `.value_counts()`.

- **polars_stats.py**  
  Leverages Polars, a high-performance DataFrame library optimized for speed and memory efficiency. Employs methods equivalent to Pandas to provide fast descriptive statistics.

- **visualize_data.ipynb**  
  A Jupyter Notebook containing exploratory visualizations complementing the statistical summaries, including histograms, boxplots, and bar charts.

- **README.md**  
  This documentation file describing project purpose, structure, and usage.

---

## Datasets

This analysis uses three large-scale datasets derived from social media activity and advertisements during the 2024 U.S. presidential election:

- **2024_fb_ads_president_scored_anon.csv** — Facebook political ad records with metadata and scoring features.  
- **2024_fb_posts_president_scored_anon.csv** — Facebook posts related to presidential campaigns with engagement metrics.  
- **2024_tw_posts_president_scored_anon.csv** — Twitter posts about presidential campaigns, including sentiment and topic analysis.

> **Note:** Due to the large size of datasets (100MB+), they are not included in this repository and should be downloaded separately via the provided link below.

---

## How to Run

### Download the datasets  
Download the datasets from the provided [link](https://drive.google.com/file/d/1Jq0fPb-tq76Ee_RtM58fT0_M3o-JDBwe/view?usp=sharing)

### Prerequisites  
- Python 3.8 or later installed.  
- Required libraries (for pandas and polars scripts):  
  ```bash
  pip install pandas polars matplotlib seaborn
  ```

```

```
## Running the Scripts
 From your terminal or command prompt, navigate to the project directory and execute:
 
  ```bash
   python pure_python_stats.py <dataset.csv>
   python pandas_stats.py <dataset.csv>
   python polars_stats.py <dataset.csv>
  ```

Example:

  ```bash
    python pandas_stats.py 2024_fb_ads_president_scored_anon.csv
  ```

Replace <dataset.csv> with the path to the dataset file you want to analyze.

```


```
## Summary Statistics Output

Each script outputs summary statistics including:

- **Numeric columns:** count, mean, standard deviation, min, max, quartiles.  
- **Categorical columns:** unique value counts, top frequent values.  
- **Grouped statistics** by key identifiers such as `page_id` or `(page_id, ad_id)`.

---

## Visualization

Open and run the `visualize_data.ipynb` notebook in Jupyter or VS Code to generate visual summaries, including:

- Distributions of numeric variables through histograms and boxplots  
- Frequency counts of top categories for categorical columns  
- Comparative insights to guide exploratory data analysis and decision-making

---

## What Each Script Does

### pure_python_stats.py
- Reads CSV data using Python's `csv` module.  
- Calculates descriptive statistics manually:  
  - Numeric fields: count, mean, min, max, quartiles.  
  - Categorical fields: counts of unique values and most frequent entries.  
- Performs grouping on key columns to provide aggregated statistics.  
- Demonstrates foundational statistical logic without third-party libraries.  
- Ideal for learning or restricted environments.

### pandas_stats.py
- Uses `pandas.read_csv()` for efficient data loading.  
- Employs `DataFrame.describe()`, `nunique()`, and `value_counts()` for quick stats.  
- Uses `groupby` operations for grouped summaries.  
- Balances code brevity with good performance on moderate datasets.  
- Suitable for most data science workflows.

### polars_stats.py
- Reads CSV data using Polars for fast parsing.  
- Uses Polars’ native functions like `.describe()`, `.n_unique()`, and `.value_counts()`.  
- Handles group-by operations efficiently, beneficial for very large datasets.  
- Shows how modern DataFrame engines optimize memory and CPU usage.  
- Recommended for production scenarios or extremely large data.

---

## Key Findings & Insights

- **Reproducibility:** Identical statistical summaries are achievable using all three approaches, validating the correctness of pure Python implementations and third-party libraries.

- **Performance Comparison:**  
  - Pure Python is clear but slow and verbose.  
  - Pandas offers an excellent balance between usability and speed for typical dataset sizes.  
  - Polars outperforms Pandas in speed and memory efficiency on large-scale datasets.

- **Usability:**  
  - Pandas benefits from an extensive ecosystem with many tutorials and integrations.  
  - Polars is promising for future-proofing big data analytics workflows.

---

## Challenges

- Ensuring consistent handling of missing data and data types across tools.  
- Managing memory efficiently when processing millions of rows.

---

## Additional Notes

- This project can be adapted to any CSV dataset requiring similar descriptive statistics and group-wise analysis.  
- Visualization notebooks complement the numeric summaries for richer data understanding.  
- Contributions and improvements to optimize pure Python implementations or expand visualizations are welcome.

---

## Author

**Lakshmi Peram**  
Email: [lperam@syr.edu](mailto:lperam@syr.edu)

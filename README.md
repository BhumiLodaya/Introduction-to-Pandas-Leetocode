# 🐍 Introduction to Pandas: Data Manipulation Fundamentals

---
## 🏆 Project Overview and Achievement

This repository documents the foundational exercises completed for the "Introduction to Pandas" certification. The project focuses on mastering the core principles of data structure, cleaning, modification, and aggregation using the **Pandas** library in Python.

**Status:** **[Insert Today's Date]**
**Badge Earned:** 🏅 **Introduction to Pandas**

---
## 🛠️ Core Concepts Mastered

This collection of solutions demonstrates proficiency in the following essential data science operations:

### 1. Data Structure & Type Control
* **DataFrame Construction:** Creating DataFrames from raw 2D lists.
* **Column Renaming:** Structurally updating multiple column names using the `.rename()` method with dictionary mapping.
* **Data Type Correction:** Modifying column data types (e.g., Float to Integer) using the `.astype()` method.

### 2. Data Cleaning and Preparation
* **Missing Data Imputation:** Replacing missing values (`NaN`) in specific columns using **`.fillna()`**.
* **Duplicate Removal:** Identifying and removing duplicate rows based on a subset of columns using **`.drop_duplicates()`**.

### 3. Data Manipulation and Vectorization
* **Vectorized Operations:** Modifying entire columns efficiently (e.g., doubling the `salary` column) using direct assignment and arithmetic operations.
* **Data Reshaping:** Transforming data using both **`.pivot()`** (wide format) and **`.melt()`** (long format).

### 4. Filtering, Sorting, and Aggregation
* **Boolean Indexing:** Performing complex row selection using conditions (e.g., `weight > 100`).
* **Sorting:** Ordering data by column values in ascending or descending order using **`.sort_values()`**.
* **Aggregation:** Grouping data and performing counts or calculations using **`.groupby()`**.

---
## 💻 Key Solution Examples

The following code snippets showcase mastery of combining multiple operations into efficient, chained methods:

### 1. Complex Filtering and Sorting
*Goal: List animals weighing over 100 kg, sorted by weight (descending).*

```python
def select_and_sort_heavy_animals(animals: pd.DataFrame) -> pd.DataFrame:
    # Filter rows -> Sort values -> Project the 'name' column
    return animals[animals['weight'] > 100].sort_values(
        by='weight', 
        ascending=False
    )[['name']]

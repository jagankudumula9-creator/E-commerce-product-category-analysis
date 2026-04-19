# =========================================================
# E-COMMERCE PRODUCT CATEGORY ANALYSIS
# =========================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (7,4)

# -------------------- LOAD DATA ---------------------------
df = pd.read_csv("ecommerce_data.csv")

# -------------------- DATA CLEANING -----------------------
df['category'] = df['category'].fillna('Unknown')
df['rating'] = df['rating'].fillna(df['rating'].mean())
df['price'] = df['price'].fillna(df['price'].median())

# -------------------- FEATURE ENGINEERING -----------------
bins = [0, 50, 100, 200, 500, 1000]
labels = ['0-50', '51-100', '101-200', '201-500', '500+']
df['price_range'] = pd.cut(df['price'], bins=bins, labels=labels)

# -------------------- SUMMARY -----------------------------
print("\n====== SUMMARY ======")
print("Total Products:", len(df))
print("Categories:", df['category'].nunique())
print("Average Price:", round(df['price'].mean(), 2))

# -------------------- SAVE COMBINED PLOTS -----------------
plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
sns.countplot(y='category', data=df)
plt.title("Category Distribution")

plt.subplot(2,2,2)
sns.boxplot(x='category', y='price', data=df)
plt.xticks(rotation=45)
plt.title("Price by Category")

plt.subplot(2,2,3)
sns.histplot(df['rating'], bins=10, kde=True)
plt.title("Rating Distribution")

plt.subplot(2,2,4)
sns.countplot(x='price_range', data=df)
plt.title("Price Range")

plt.tight_layout()
plt.savefig("pda output.png")   # ✅ Important
plt.show()
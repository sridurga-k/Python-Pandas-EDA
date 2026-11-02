import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#structures
x = pd.read_csv("/content/smartphones_cleaned_v6.csv")
print("data load successfully")
print("First 5 rows:",x.head(5))
print("Shapes of datasets:",x.shape)
print("column data types:")
print(x.dtypes)
print("Memory usage ",x.info())

#missing values
missing_data = pd.DataFrame(
    {
        "Missing Count": x.isnull().sum(),
        "Missing Percentage": (x.isnull().sum() / len(x)) * 100,
    }
)
print(missing_data[missing_data["Missing Count"] > 0])

# Visualizing missing values using a heatmap
plt.figure(figsize=(10, 5))
sns.heatmap(x.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Values Heatmap")
plt.show()

#Summary Statistics & Categorical Breakdowns
print(x["price"].describe())
print("Content Types:\n", x["model"].value_counts(normalize=True) * 100)
print("\nTop 5 Ratings:\n", x["rating"].value_counts().head(5))

#Exploratory Data Visualizations
fig, axes = plt.subplots(3, 2, figsize=(16, 18))

# Viz 1: Price Distribution
sns.histplot(
    x["price"].dropna(), bins=30, kde=True, ax=axes[0, 0], color="royalblue"
)
axes[0, 0].set_title(
    "Distribution of Smartphone Prices", fontsize=14, fontweight="bold"
)
axes[0, 0].set_xlabel("Price (INR)", fontsize=12)
axes[0, 0].set_ylabel("Count", fontsize=12)

# Viz 2: Price vs Rating (Colored by 5G)
sns.scatterplot(
    data=x,
    x="rating",
    y="price",
    hue="has_5g",
    alpha=0.7,
    ax=axes[0, 1],
    palette="deep",
)
axes[0, 1].set_title(
    "Smartphone Price vs. Rating (colored by 5G)",
    fontsize=14,
    fontweight="bold",
)
axes[0, 1].set_xlabel("Rating", fontsize=12)
axes[0, 1].set_ylabel("Price (INR)", fontsize=12)

# Viz 3: Top 10 Brands by Model Count
top_brands = x["brand_name"].value_counts().head(10)
sns.barplot(
    x=top_brands.values, y=top_brands.index, ax=axes[1, 0], palette="viridis"
)
axes[1, 0].set_title(
    "Top 10 Smartphone Brands by Model Count", fontsize=14, fontweight="bold"
)
axes[1, 0].set_xlabel("Number of Models", fontsize=12)
axes[1, 0].set_ylabel("Brand Name", fontsize=12)

# Viz 4: Battery Capacity Distribution across OS
sns.boxplot(
    data=x, x="os", y="battery_capacity", ax=axes[1, 1], palette="Set2"
)
axes[1, 1].set_title(
    "Battery Capacity Distribution across Operating Systems",
    fontsize=14,
    fontweight="bold",
)
axes[1, 1].set_xlabel("Operating System", fontsize=12)
axes[1, 1].set_ylabel("Battery Capacity (mAh)", fontsize=12)

# Viz 5: RAM Capacity vs Price Distribution
common_rams = [4, 6, 8, 12, 16]
df_ram = x[x["ram_capacity"].isin(common_rams)]
sns.boxplot(
    data=df_ram,
    x="ram_capacity",
    y="price",
    ax=axes[2, 0],
    palette="coolwarm",
)
axes[2, 0].set_title(
    "Price Distribution across RAM Capacities", fontsize=14, fontweight="bold"
)
axes[2, 0].set_xlabel("RAM Capacity (GB)", fontsize=12)
axes[2, 0].set_ylabel("Price (INR)", fontsize=12)

# Viz 6: Correlation Matrix of Key Numeric Features
corr = x[numeric_cols].corr()
sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    ax=axes[2, 1],
    cbar_kws={"shrink": 0.8},
)
axes[2, 1].set_title(
    "Correlation Matrix of Key Numeric Features",
    fontsize=14,
    fontweight="bold",
)

plt.tight_layout()
plt.savefig("smartphone_eda_visualizations.png", dpi=300)
plt.show()


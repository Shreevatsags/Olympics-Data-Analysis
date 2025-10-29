# 🏅 Olympics Data Cleaning, Analysis & Visualization
# ---------------------------------------------------
# Author: Shreevatsa
# Description: Performed data cleaning, EDA, and visualization on Olympics dataset
# to uncover trends, athlete insights, and medal statistics.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------
# 🔹 Load Dataset
# ---------------------------------------------------
try:
    df = pd.read_csv("olympics.csv", encoding='latin1')
    print("✅ Dataset Loaded Successfully")
except Exception as e:
    print("❌ Error loading dataset:", e)
    exit()

print(df.head())

# ---------------------------------------------------
# 🔹 Data Cleaning
# ---------------------------------------------------
df.columns = df.columns.str.strip()   # Clean column names (remove spaces)
df.drop_duplicates(inplace=True)

# Handle missing values
for col in ["Athlete", "Country", "Sport", "Event", "Medal"]:
    df = df[df[col].notna()]

# Fill missing numeric columns if present
if "Year" in df.columns:
    df["Year"].fillna(df["Year"].mode()[0], inplace=True)

print("\n✅ Data Cleaning Completed")
print(df.info())

# ---------------------------------------------------
# 🔹 Basic Summary
# ---------------------------------------------------
print("\n📊 Dataset Overview:")
print("🔸 Total Records:", len(df))
print("🔸 Total Unique Athletes:", df['Athlete'].nunique())
print("🔸 Total Sports:", df['Sport'].nunique())
print("🔸 Total Events:", df['Event'].nunique())
print("🔸 Total Countries:", df['Country'].nunique())

# ---------------------------------------------------
# 1️⃣ Medals by Country
# ---------------------------------------------------
top_countries = df['Country'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_countries.values, y=top_countries.index, palette="viridis")
plt.title("🏅 Top 10 Countries by Total Medals")
plt.xlabel("Number of Medals")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

# ---------------------------------------------------
# 2️⃣ Medals Over Time
# ---------------------------------------------------
medals_by_year = df.groupby("Year")["Medal"].count()
plt.figure(figsize=(12, 6))
plt.plot(medals_by_year.index, medals_by_year.values, marker='o', color='crimson')
plt.title("📈 Medals Over the Years")
plt.xlabel("Year")
plt.ylabel("Total Medals")
plt.grid(True)
plt.tight_layout()
plt.show()

# ---------------------------------------------------
# 3️⃣ Gender Distribution
# ---------------------------------------------------
plt.figure(figsize=(6, 6))
df["Gender"].value_counts().plot.pie(autopct="%1.1f%%", colors=["skyblue", "lightpink"])
plt.title("⚧ Gender Distribution of Athletes")
plt.ylabel("")
plt.show()

# ---------------------------------------------------
# 4️⃣ Top 10 Sports with Most Medals
# ---------------------------------------------------
top_sports = df["Sport"].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_sports.values, y=top_sports.index, palette="magma")
plt.title("🎯 Top 10 Sports with Most Medals")
plt.xlabel("Number of Medals")
plt.ylabel("Sport")
plt.tight_layout()
plt.show()

# ---------------------------------------------------
# 5️⃣ Medals by Gender and Sport
# ---------------------------------------------------
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x="Sport", hue="Gender", order=df["Sport"].value_counts().index[:8])
plt.title("⚧ Gender-wise Medal Distribution per Sport")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------------------------------------------------
# 6️⃣ Top 5 Countries - Medal Trends Over Time
# ---------------------------------------------------
top5 = df["Country"].value_counts().head(5).index
plt.figure(figsize=(12, 6))
for country in top5:
    country_data = df[df["Country"] == country].groupby("Year")["Medal"].count()
    plt.plot(country_data.index, country_data.values, marker='o', label=country)
plt.title("🌍 Medal Trends Over Time (Top 5 Countries)")
plt.xlabel("Year")
plt.ylabel("Number of Medals")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ---------------------------------------------------
# 7️⃣ Save Cleaned Dataset
# ---------------------------------------------------
df.to_csv("cleaned_olympics_data.csv", index=False)
print("\n✅ Cleaned data saved as 'cleaned_olympics_data.csv'")

print("\n🎉 Analysis Completed Successfully!")

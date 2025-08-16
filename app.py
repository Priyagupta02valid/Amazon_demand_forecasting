# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------
# LOAD DATASET
# -----------------------
df = pd.read_csv("amazon.csv")

# -----------------------
# CLEAN DATA
# -----------------------
# Remove currency symbols, commas and convert to float
df['actual_price'] = df['actual_price'].astype(str).str.replace('₹','').str.replace(',','').astype(float)
df['discounted_price'] = df['discounted_price'].astype(str).str.replace('₹','').str.replace(',','').astype(float)
df['discount_percentage'] = df['discount_percentage'].astype(str).str.replace('%','').astype(float)
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')  # handle any non-numeric ratings

# -----------------------
# SIDEBAR FILTER
# -----------------------
st.sidebar.header("Filter Products")
category = st.sidebar.selectbox("Select Category", df["category"].unique())
filtered_df = df[df['category'] == category]

# -----------------------
# DASHBOARD METRICS
# -----------------------
st.title("📊 Amazon Sales Dashboard")
st.subheader(f"Overview of {category}")

col1, col2, col3 = st.columns(3)
col1.metric("Total Products", len(filtered_df))
col2.metric("Average Price", f"₹{filtered_df['actual_price'].mean():.2f}")
col3.metric("Average Discount %", f"{filtered_df['discount_percentage'].mean():.2f}%")

# -----------------------
# TOP PRODUCTS BY RATING
# -----------------------
st.subheader("Top 10 Products by Rating")
top_products = filtered_df.sort_values(by='rating', ascending=False).head(10)
st.table(top_products[['product_name', 'rating', 'rating_count', 'actual_price', 'discounted_price']])

# -----------------------
# PRICE DISTRIBUTION
# -----------------------
st.subheader("Price Distribution")
fig, ax = plt.subplots()
sns.histplot(filtered_df['actual_price'], bins=20, kde=True, ax=ax)
ax.set_xlabel("Actual Price")
ax.set_ylabel("Number of Products")
st.pyplot(fig)

# -----------------------
# RATING DISTRIBUTION
# -----------------------
st.subheader("Rating Distribution")
fig2, ax2 = plt.subplots()
sns.countplot(x='rating', data=filtered_df, ax=ax2)
ax2.set_xlabel("Rating")
ax2.set_ylabel("Number of Products")
st.pyplot(fig2)

# -----------------------
# END OF DASHBOARD
# -----------------------

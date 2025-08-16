 
 
# 📊 Amazon Sales Dashboard

**Overview:**
This project is an interactive **Amazon Sales Dashboard** built using **Python**, **Pandas**, **Matplotlib**, **Seaborn**, and **Streamlit**. It allows users to explore Amazon product data, visualize pricing, discounts, and ratings, and gain insights into product performance across different categories.

**Key Features:**

* Filter products by category using a sidebar.
* View key metrics: total products, average price, and average discount percentage.
* Display **top-rated products** in a table format.
* Visualize **price distribution** using histograms.
* Visualize **rating distribution** with count plots.
* Fully interactive dashboard deployable with **Streamlit**.

**Technologies Used:**

* Python
* Pandas (data cleaning & analysis)
* Matplotlib & Seaborn (visualizations)
* Streamlit (interactive dashboard & deployment)

**Dataset:**
The dashboard uses a CSV dataset (`amazon.csv`) containing Amazon product information with columns like `product_name`, `category`, `actual_price`, `discounted_price`, `rating`, `review_content`, and more.

**How to Run:**

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
streamlit run app.py
```

4. Open the browser at [http://localhost:8501](http://localhost:8501).

**Future Enhancements:**

* Include product images in the dashboard.
* Add interactive search and sorting for products.
* Implement sentiment analysis on reviews.
* Deploy on **Streamlit Cloud** or **Heroku** for public access.

**Author:**
Priya Gupta
 

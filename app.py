import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

sales_data = pd.read_csv("Datasets/test_dataset_1.csv")
sentiment_data = pd.read_csv("Datasets/category_avg_net_sentiments.csv")

category_sales = sales_data.groupby('Category')['TotalSales'].sum().reset_index()
category_sales = category_sales.sort_values(by='TotalSales', ascending=False)
category_sales['Rank by Total Sales'] = range(1, len(category_sales) + 1)

sentiment_data = sentiment_data.merge(category_sales[['Category', 'Rank by Total Sales']], on='Category')

st.sidebar.title("Walmart Product Analysis")
categories = sales_data['Category'].unique()
selected_category = st.sidebar.selectbox("Choose Category", categories)

st.header("Category Analysis")
grouped_stats = sales_data.groupby(['Category']).agg(
    TotalSales_Median=('TotalSales', 'median'),
    TotalSales_Sum=('TotalSales', 'sum'),
    TotalSales_Min=('TotalSales', 'min'),
    TotalSales_Max=('TotalSales', 'max')
).reset_index()

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.header("Total Sales Median")
    st.write(grouped_stats['TotalSales_Median'].mean())
with col2:
    st.header("Total Sales Sum")
    st.write(grouped_stats['TotalSales_Sum'].sum())
with col3:
    st.header("Total Sales Min")
    st.write(grouped_stats['TotalSales_Min'].min())
with col4:
    st.header("Total Sales Max")
    st.write(grouped_stats['TotalSales_Max'].max())

col1, col2 = st.columns(2)
with col1:
    top_categories = sales_data.groupby('Category')['TotalSales'].sum().nlargest(5)
    fig, ax = plt.subplots()
    sns.barplot(x=top_categories.values, y=top_categories.index, ax=ax, palette="husl")
    ax.set_xlabel('Total Sales')
    ax.set_ylabel('Category')
    ax.set_title('Top 5 Categories by Sales')
    st.pyplot(fig)

with col2:
    st.write("Top 5 Categories by Sentiment")
    top_5_sentiment = sentiment_data.sort_values(by='SentimentScore1_10', ascending=False).head(5)
    top_5_sentiment_display = top_5_sentiment[['Category', 'SentimentScore1_10', 'Rank by Total Sales']]
    st.dataframe(top_5_sentiment_display, use_container_width=True)

if st.sidebar.button("Show Analysis"):
    st.header(f"Analysis for {selected_category}")

    category_data = sales_data[sales_data['Category'] == selected_category]

    category_data = category_data.merge(sentiment_data[['Category', 'SentimentScore1_10']], on='Category', how='left')

    #wordcloud
    st.subheader(f"Word Cloud for Reviews in {selected_category}")
    all_reviews = " ".join(review for review in category_data['ReviewText'])
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_reviews)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)



    st.subheader(f"Analysis by Sentiment Score in {selected_category}")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Top 5 products")
        top_5_sentiment_products = category_data.sort_values(by='SentimentScore1_10', ascending=False).head(5)
        fig, ax = plt.subplots()
        sns.barplot(x='SentimentScore1_10', y='ProductName', data=top_5_sentiment_products, ax=ax, palette="Blues_d")
        ax.set_title("Top 5 Products by Sentiment Score")
        for index, value in enumerate(top_5_sentiment_products['SentimentScore1_10']):
            ax.text(value, index, f'{value:.2f}', va='center')
        st.pyplot(fig)

    with col2:
        st.write("Bottom 5 products")
        bottom_5_sentiment_products = category_data.sort_values(by='SentimentScore1_10').head(5)
        fig, ax = plt.subplots()
        sns.barplot(x='SentimentScore1_10', y='ProductName', data=bottom_5_sentiment_products, ax=ax, palette="Reds_d")
        ax.set_title("Bottom 5 Products by Sentiment Score")
        for index, value in enumerate(bottom_5_sentiment_products['SentimentScore1_10']):
            ax.text(value, index, f'{value:.2f}', va='center')
        st.pyplot(fig)

    st.subheader(f"Analysis by Sales in {selected_category}")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Top 5 products")
        top_5_sales_products = category_data.sort_values(by='TotalSales', ascending=False).head(5)
        fig, ax = plt.subplots()
        sns.barplot(x='TotalSales', y='ProductName', data=top_5_sales_products, ax=ax, palette="Greens_d")
        ax.set_title("Top 5 Products by Sales")
        for index, value in enumerate(top_5_sales_products['TotalSales']):
            ax.text(value, index, f'{value:.2f}', va='center')
        st.pyplot(fig)

    with col2:
        st.write("Bottom 5 products")
        bottom_5_sales_products = category_data.sort_values(by='TotalSales').head(5)
        fig, ax = plt.subplots()
        sns.barplot(x='TotalSales', y='ProductName', data=bottom_5_sales_products, ax=ax, palette="Oranges_d")
        ax.set_title("Bottom 5 Products by Sales")
        for index, value in enumerate(bottom_5_sales_products['TotalSales']):
            ax.text(value, index, f'{value:.2f}', va='center')
        st.pyplot(fig)


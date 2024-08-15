import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

sales_data = pd.read_csv("Datasets/test_dataset_1.csv")
sentiment_data = pd.read_csv("Datasets/category_avg_net_sentiments.csv")
categories = sales_data['Category'].unique()
st.sidebar.title("Category Analysis")
selected_category = st.sidebar.selectbox("Choose Category for Analysis", categories)

st.title(f"Analysis for {selected_category}")

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
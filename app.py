import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

st.sidebar.title("Walmart Product Analysis")
sales_data = pd.read_csv("Datasets/test_dataset_1.csv")
categories = sales_data['Category'].unique()
selected_category = st.sidebar.selectbox("Choose Category", categories)

st.title("Category Analysis")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.header("Stats A")
with col2:
    st.header("Stats B")
with col3:
    st.header("Stats C")
with col4:
    st.header("Stats D")


col1, col2 = st.columns(2)
with col1: 
    top_categories = sales_data.groupby('Category')['TotalSales'].sum().nlargest(5)
    fig, ax = plt.subplots()
    sns.barplot(x=top_categories.values, y=top_categories.index, ax=ax)
    ax.set_xlabel('Total Sales')
    ax.set_ylabel('Category')
    ax.set_title('Top 5 Categories by Sales')
    st.pyplot(fig)

with col2:
    st.write("dataframe of stats")

# Show analysis button
if st.sidebar.button("Show Analysis"):
    st.header(f"Analysis for {selected_category}")

    st.write("Description to be added later...")

    col1, col2 = st.columns(2)

    with col1:
        st.write("basic stats")

    with col2:
        st.write("data frame with values")
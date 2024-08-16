import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Homepage")
st.divider()
st.subheader("Project Overview")

st.write('''Welcome to our comprehensive retail analytics platform, designed to empower businesses with actionable insights through advanced data science techniques. Our platform leverages sentiment analysis, sales analysis, and demand forecasting to help you make informed decisions that drive growth and efficiency.

Features:

1. Sentiment and Sales Analysis:
   - Gain a clear understanding of how your product categories and individual products are performing.
   - Visualize the best and worst-performing categories and products with intuitive bar charts and key statistics.
   - Leverage sentiment analysis to assess customer satisfaction and identify areas for improvement.

2. Sales Forecasting:
   - Plan ahead with confidence using our sales forecasting tool.
   - View predicted future sales on a yearly basis, allowing you to make data-driven decisions about inventory, marketing, and procurement.''')

st.subheader("Why Use This Platform?")

st.write('''- Data-Driven Decisions: Our platform provides a robust analytical foundation to help you optimize your product offerings, anticipate customer needs, and enhance overall business performance.
- User-Friendly Interface: Easily navigate through insightful visualizations and statistical data, making complex analysis accessible to everyone.
- Future-Proofing Your Business: With accurate sales forecasts, you can stay ahead of market trends and ensure your business is always prepared for the future.

''')

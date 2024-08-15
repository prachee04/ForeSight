import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA

st.title("Demand Forecasting")
st.divider()
st.sidebar.title("Demand Forecasting")
chart = st.sidebar.selectbox("Type of chart required:", ["Line Chart", "Bar Chart"])
val = st.sidebar.slider("Select the duration for forecast: ", min_value = 1, max_value = 10, value = 5)
button = st.sidebar.button("Submit")

df = pd.read_csv("Datasets/test_dataset_2.csv")
df['OrderDate'] = pd.to_datetime(df['OrderDate'], format= "%d-%m-%Y", errors='coerce')
df = df.loc[:, ["OrderDate", "TotalSales"]]
df.set_index('OrderDate', inplace=True)
df = df.resample('Y').sum()

st.subheader("Data Preview:")
st.write(df)
fig_line = plt.figure(figsize=(14, 7))
plt.plot(df.index, df['TotalSales'], label='Actual Sales', marker='o')
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.title('Yearly Sales')
plt.legend()
plt.grid(True)
st.pyplot(fig_line)

st.divider()

#st.write(df)

train = df[:int(0.8 * len(df))]
test = df[int(0.8 * len(df)):]

#st.write(train.shape, test.shape)

model = sm.tsa.arima.ARIMA(df, order = (1,1,1))
model = model.fit()

st.subheader("Prediction on test data using ARIMA model")
pred = model.predict(start = len(train), end = len(df)-1)
st.write(pred)
fig_pred = plt.figure(figsize=(14,7))
plt.plot(df, marker = 'o')
plt.plot(pred, marker = 'o')
plt.grid()
plt.legend(['Actual','Predicted'])
st.pyplot(fig_pred)

st.divider()


if button:
    st.subheader(f"Forecasting for {val} years")
    future = pd.date_range(start=df.index[-1], periods=val, freq='Y')
    future_df = pd.DataFrame(future, columns = ["Date"])
    
    forecast = model.get_forecast(steps=val)
    forecast_df = forecast.summary_frame()
    
    future_df['Forecast'] = forecast_df['mean'].values

    st.write(future_df)

    fig_forecast = plt.figure(figsize=(10, 6))
    plt.plot(df, label='Historical Data')
    plt.plot(future_df['Date'], future_df['Forecast'], label='Forecast', color='red')
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.legend()
    st.pyplot(fig_forecast)
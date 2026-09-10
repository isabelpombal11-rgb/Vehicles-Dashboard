import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('US Used Car Listings Dashboard')

hist_button = st.button('Create histogram')

if hist_button:
    st.write('Creating a histogram of vehicle mileage across all car listings')
    fig = px.histogram(car_data, x="odometer", labels={"odometer": "Odometer (miles)"},
                       title="Distribution of vehicle mileage")
    fig.update_layout(yaxis_title="Number of listings")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Create scatter plot')

if scatter_button:
    st.write('Creating a scatter plot of mileage against asking price')
    fig = px.scatter(car_data, x="odometer", y="price",
                     labels={"odometer": "Odometer (miles)", "price": "Price (USD)"},
                     title="Asking price vs mileage")
    st.plotly_chart(fig, use_container_width=True)

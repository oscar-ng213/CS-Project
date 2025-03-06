import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Bar chart")
st.markdown("Function 2: Bar Chart")
st.sidebar.header("Bar Chart")
st.write("This function illustrates a bar chart")

dataIn = pd.read_csv("cleanedDF.csv")
dataIn['dt'] = pd.to_datetime(dataIn['dt'])
validCountryList = list(dataIn['Country'].unique())

st.header("Select a country")
countryInput = st.selectbox("Select a country", validCountryList)
year = st.slider("Select a year", 2000, 2013)

def function2(country, year):
    countryData = dataIn[dataIn['Country'] == country]
    yearData = countryData[countryData['dt'].dt.year == year]
    monthAver = yearData.groupby(yearData['dt'].dt.month)['AverageTemperature'].mean()
    monthMap = {1:"Jan", 2:"Feb", 3:"Mar", 4:"Apr", 5:"May", 6:"Jun",
                 7:"Jul", 8:"Aug", 9:"Sep", 10:"Oct", 11:"Nov", 12:"Dec"}
    monthAver.index = monthAver.index.map(monthMap)
    order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
             "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    monthAver = monthAver.reindex(order).dropna()
    monthAver.index = pd.CategoricalIndex(monthAver.index, categories=order, ordered=True)
    monthAver = monthAver.sort_index()
    return monthAver

if st.button("Analyse Data"):
    monthlyData = function2(countryInput, year)
    st.write(f"Monthly Mean Temperature in {countryInput} in {year}")
    st.bar_chart(monthlyData)

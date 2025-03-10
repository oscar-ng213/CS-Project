#Function 2 (Bar chart): 

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

def function2(countryInput, year):                                                
    countryData = dataIn[(dataIn['Country'] == countryInput) & (dataIn['dt'].dt.year == year)]
    monthlyData = countryData.groupby(countryData['dt'].dt.strftime('%b'))['AverageTemperature'].mean()  #Calculae the mean temperature              
    monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] 
    monthlyData = monthlyData.reindex(monthList).dropna() #Reorder data based on monthList, drop months with no data
    monthlyData.index = pd.CategoricalIndex(monthlyData.index, categories=monthList, ordered=True)
    monthlyData = monthlyData.sort_index()
    return monthlyData

if st.button("Analyse Data"):
    monthlyData = function2(countryInput, year)
    st.write(f"Monthly Mean Temperature in {countryInput} in {year}")
    st.bar_chart(monthlyData)

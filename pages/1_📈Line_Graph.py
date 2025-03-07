#Function 1: 
#--------------------------------------------------------------------------------------
#A full dictionary of temperature sorted by Country {'Ireland': [12,13,14], 'United Kingdom': [10,12,13].....}

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(page_title="Pie chart")
st.title('Function 1')
st.markdown("Function 1: Line chart")
st.sidebar.header("Line graph")
st.write("""This function illustrates a line graph""")

dataIn = pd.read_csv("cleanedDF.csv")
dataIn['dt'] = pd.to_datetime(dataIn['dt'])
validCountryList = list(dataIn['Country'].unique())

st.header("Select countr(ies)")
listOfCountry = st.multiselect("Select Countries", validCountryList)
yearRange = st.slider("Select Year Range", 2000, 2013, (2000, 2010))

def function1(listOfCountry, yearRangeFrom, yearRangeTo):
    countryMean = {}
    listOfYears = list(range(yearRangeFrom, yearRangeTo + 1))
    countryData = dataIn[(dataIn['Country'].isin(listOfCountry)) & 
                         (dataIn['dt'].dt.year.between(yearRangeFrom, yearRangeTo))]
    for country in listOfCountry:
        data = countryData[countryData['Country'] == country]
        yearData = data.groupby(data['dt'].dt.year)['AverageTemperature'].mean()
        countryMean[country] = yearData.reindex(listOfYears).round(2)   
    return countryMean, listOfYears

if st.button("Analyse Data"):
    if listOfCountry == []:
        st.write('You need at least 1 country :/')
    else:
        data, listOfYears = function1(listOfCountry, yearRange[0], yearRange[1])
        plt.figure(figsize=(12, 6))
        for country, temperatures in data.items():
            plt.plot(listOfYears, temperatures, marker='o', linestyle='-', label=country)
        st.write('Annual Mean Temperature Trends by Country')
        plt.title('Annual Mean Temperature Trends by Country')
        plt.xlabel('Year')
        plt.ylabel('Mean Annual Temperature (°C)')
        plt.legend(title="Countries", loc='upper left')
        plt.grid(True)  
        plt.xticks(listOfYears)  
        if data:
            minTemp = min([min(temps) for temps in data.values() if not temps.isna().all()]) - 1
            maxTemp = max([max(temps) for temps in data.values() if not temps.isna().all()]) + 2
            plt.yticks(np.linspace(minTemp, maxTemp, 10))
        st.pyplot(plt)
#Function 4 Linear Regression ( Recommendation AR3 )
#---------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import streamlit as st

dataIn =  pd.read_csv("cleanedDF.csv")
dataIn['dt'] = pd.to_datetime(dataIn['dt'])
validCountryList = list(dataIn['Country'].unique())

st.set_page_config(page_title="Pie chart")

st.markdown("Function 4: Prediction")
st.sidebar.header("Linear Regression")
st.write("""This function finds the line of best fit of yearly mean temperature between 2000-2009,""")
st.write("""If the slope of the line is greater than 0.02 (More than 0.2°C increase per decade)""")
st.write("""your country may have a greater rate of global warming than the average""")

countryInput = st.selectbox('Select a country', validCountryList)

def function4(countryInput):
    listOfYears = list(range(2000,2010))

    countryMean = []                                                                                  
    countryData = dataIn[dataIn['Country'] == countryInput]       
    for year in listOfYears:                                                        
        yearData = countryData[(countryData['dt']).dt.year == year]   
        aver = yearData['AverageTemperature'].mean()                                
        countryMean.append(round(aver, 6))
    
    xList = []
    yList = []
    xyList = []
    x2List = []
    for index in range(len(countryMean)):
        x = index + 1
        xList.append(x)
        y = countryMean[index]
        yList.append(y)
        xy = round(x * y, 6)
        xyList.append(xy)
        x2 = round(x ** 2, 6)
        x2List.append(x2)
    
    sumX = sum(xList)
    sumY = sum(yList)
    sumXY = sum(xyList)
    sumX2 = sum(x2List)

    numerator = len(countryMean) * sumXY - sumX * sumY
    denominator = len(countryMean) * sumX2 - sumX ** 2
    m = round(numerator/denominator, 6)
    b = round((sumY - m * sumX) / len(countryMean), 6)
    st.write(f'Formula: y = {m}x + {b}')
    
    if m > 0.02:
        st.write(f'Your country {countryInput} is HAS reached the critical threshold')
    else:
        st.write(f'Your country {countryInput} is HAS NOT reached the critical threshold')
    st.write(m)
    
    listOfYears = list(range(2000,2051))
    predictionMean = [round(m * (x+1) + b, 6) for x in range(len(listOfYears))]
    predictionMean[:len(countryMean)] = countryMean
    return predictionMean, listOfYears

if st.button('Analyse Data'):
    predictionMean, listOfYears = function4(countryInput)
    plt.figure(figsize=(12, 6))
    plt.scatter(listOfYears, predictionMean, marker='o', linestyle='-')
    plt.title(f'Prediction Model of {countryInput}')
    plt.xlabel('Year')
    plt.ylabel('Mean Annual Temperature (°C)')
    plt.grid(True)  # Add grid for better readability
    plt.xticks(range(2000,2051,5))  
    minTemp = min(predictionMean) -1  # Find lowest temperature and subtract 1
    maxTemp = max(predictionMean) +2 # Find highest temperature and add 2
    plt.yticks(np.linspace(minTemp, maxTemp, 10)) 
    st.pyplot(plt)

    
    

    
#Function 3 Fluctuations in mean temperature
#---------------------------------------------------------------------------------------
#Shows the range between the min and max mean temperature of countr(ies) in a year range

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Pie chart")

st.markdown("Function 3: Pie Chart")
st.sidebar.header("Pie chart")
st.write("""This function illustrates a pie chart""")

dataIn =  pd.read_csv("cleanedDF.csv")
dataIn['dt'] = pd.to_datetime(dataIn['dt'])
validCountryList = list(dataIn['Country'].unique())

st.header("Compare countries")
listOfCountry = st.multiselect("Select Countries", validCountryList)
yearRange = st.slider("Select Year Range", 2000, 2013, (2000, 2001))
print(yearRange)

countryTempsRange = []          #Universal list
explodeList = []                #A list of 0 or 0.08 representing whether data on pie chart explode or not
diffList = []                   #List of differences 


def function3(listOfCountry, yearRangeFrom, yearRangeTo):
    listOfYears = list(range(yearRangeFrom, yearRangeTo))
    for country in listOfCountry:                                                               #Go through each country
        countryData = dataIn[dataIn['Country'].isin([country])]                                 #Filter data for the current country
        yearDataFrom = countryData[countryData['dt'].dt.year == yearRangeFrom]  #Only loc the selected data equals to yearFrom within current country
        avgTempFrom = yearDataFrom['AverageTemperature'].mean()                                 #Find the mean
        yearDataTo = countryData[(countryData['dt']).dt.year == yearRangeTo]      #Only loc the selected data equals to yearTo within current country
        avgTempTo = yearDataTo['AverageTemperature'].mean()                                     #Find the mean
        diff = round((avgTempTo - avgTempFrom),3)                                               #Find the difference
        diffList.append(diff)                #Add to the list of differences
        if diff < 0:                         #If negative, explode, If not, don't explode
            explodeList.append(0.08)
            diff *= -1
        else:
            explodeList.append(0)
        countryTempsRange.append(diff)       #Data appended and ready for visualising
    return listOfYears, diffList

if st.button("Analyse Data"):
    listOfYears, diffList = function3(listOfCountry, yearRange[0], yearRange[1])

    newListOfCountry = []   #Combining listOfCountry and diffList together e.g. ['Ireland', 'United Kingdom'] and [0.025, -0.028] becomes ['Ireland 0.025', 'United Kingdom -0.028']
    counter = 0
    for cou in listOfCountry:
        newListOfCountry.append(f'{cou} {diffList[counter]}')
        counter += 1

    explodeTup = tuple(explodeList)       #For explode values, Matplotlib only takes set data type
    plt.pie(countryTempsRange, labels=newListOfCountry, autopct='%1.1f%%', explode=explodeTup, shadow=True, startangle=90, labeldistance=.9, pctdistance=0.5)
    plt.title(f'Difference of Yearly Mean Temperature {yearRange[0]} to {yearRange[1]}')
    plt.text(1.2, 0, 'Exploded means negative values', fontsize=8, verticalalignment='center', bbox=dict(facecolor='lightgray', alpha=0.5))
    plt.tight_layout()
    st.pyplot(plt)
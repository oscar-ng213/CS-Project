#Coursework Computational Artefact // Data analytics and visualisation
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dataIn = pd.read_csv('cleanedDF.CSV')
validCountryList = list(dataIn['Country'].unique())
yearRange = list(range(2000,2014))

#Function 1
def function1():
    listOfCountry = [] 
    while True:
        countryInput = input('Enter the countr(ies) to analyse (0 to exit): ').title()
        if countryInput == '0':
            if len(listOfCountry) == 0:
                print('Must enter 1 or more country')
            else:
                break
        elif countryInput not in validCountryList:
            print(f'{countryInput} is not a valid country')
        elif countryInput in listOfCountry:
            print(f"{countryInput} is already in the list.")
        else:
            listOfCountry.append(countryInput)
    while True:
        try:
            yearRangeFrom = int(input("Enter the year range (from): "))
            if yearRangeFrom in yearRange:
                break
            print("Invalid input. Please enter a year between 2000 and 2013.")
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            yearRangeTo = int(input("Enter the year range (to): "))
            if yearRangeTo in yearRange and yearRangeTo >= yearRangeFrom:
                break
            print("Invalid input. Enter a year between 2000 and 2013, and ensure it's greater than or equal to the start year.")
        except ValueError:
            print("Please enter a valid number.")

    listOfYears = list(range(yearRangeFrom, yearRangeTo + 1))
    
    countryMean = {}                                                  
    for country in listOfCountry:                                    
        countryData = dataIn[dataIn['Country'].isin([country])]       
        countryTemps = []
        for year in listOfYears:                                                        
            yearData = countryData[pd.to_datetime(countryData['dt']).dt.year == year]
            aver = yearData['AverageTemperature'].mean()                          
            countryTemps.append(round(aver, 2))
        countryMean[country] = countryTemps                    
    
    plt.figure(figsize=(12, 6))

    for country, temperatures in countryMean.items():
        plt.plot(listOfYears, temperatures, marker='o', linestyle='-', label=country)

    plt.title('Annual Mean Temperature Trends by Country')
    plt.xlabel('Year')
    plt.ylabel('Mean Annual Temperature (°C)')
    plt.legend(title="Countries", loc='upper left')
    plt.grid(True)  
    plt.xticks(listOfYears)  
    min_temp = min([min(temps) for temps in countryMean.values()]) - 1 
    max_temp = max([max(temps) for temps in countryMean.values()]) + 2  
    plt.yticks(range(int(min_temp), int(max_temp), 2))
    plt.show()
    
#Function 2 Monthly temperature cycle in a country

def function2():  
    while True:
        countryInput = input('Enter a country: ').title()
        if countryInput not in validCountryList:
            print(f'{countryInput} is not a valid country')
        else:
            country = countryInput
            break
    while True:
        try:
            year = int(input("Enter a year"))
            if year in yearRange:
                break
            print("Invalid input. Please enter a year between 2000 and 2013.")
        except ValueError:
            print("Please enter a valid number.")
                                       
    dataIn['dt'] = pd.to_datetime(dataIn['dt'])                                 
    countryData = dataIn[dataIn['Country'] == country]                         
    yearData = countryData[pd.to_datetime(countryData['dt']).dt.year == year]                                   

    monthlyData = yearData.groupby(yearData['dt'].dt.month)['AverageTemperature'].mean()             
    monthlyData = monthlyData.reindex(range(1,13))                                        
    monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    plt.bar(monthList, monthlyData)
    plt.xlabel('Months')
    plt.ylabel('Temperature (°C)')
    plt.title(f'Monthly Mean Temperature in {country} in {year}')
    plt.grid(True, linestyle='--')
    plt.show()

#Function 3 Fluctuations in mean temperature

def function3():
    listOfCountry = [] 
    while True:
        countryInput = input('Enter the countr(ies) to analyse (0 to exit): ').title()
        if countryInput == '0':
            if len(listOfCountry) <= 1:
                print('Must enter 2 or more country')
            else:
                break
        elif countryInput not in validCountryList:
            print(f'{countryInput} is not a valid country')
        elif countryInput in listOfCountry:
            print(f"{countryInput} is already in the list.")
        else:
            listOfCountry.append(countryInput)
    while True:
        try:
            yearRangeFrom = int(input("Enter the year range (from): "))
            if yearRangeFrom in yearRange:
                break
            print("Invalid input. Please enter a year between 2000 and 2013.")
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            yearRangeTo = int(input("Enter the year range (to): "))
            if yearRangeTo in yearRange and yearRangeTo >= yearRangeFrom:
                break
            print("Invalid input. Enter a year between 2000 and 2013, and ensure it's greater than or equal to the start year.")
        except ValueError:
            print("Please enter a valid number.")                

    countryTempsRange = []         
    explodeList = []             
    diffList = []

    for country in listOfCountry:
        
        countryData = dataIn[dataIn['Country'].isin([country])]                                
        yearDataFrom = countryData[pd.to_datetime(countryData['dt']).dt.year == yearRangeFrom] 
        avgTempFrom = yearDataFrom['AverageTemperature'].mean()                                
        yearDataTo = countryData[pd.to_datetime(countryData['dt']).dt.year == yearRangeTo]      
        avgTempTo = yearDataTo['AverageTemperature'].mean()                                    
        diff = round((avgTempTo - avgTempFrom),3)                                              
        diffList.append(diff)                
        if diff < 0:                        
            explodeList.append(0.08)
            diff *= -1
        else:
            explodeList.append(0)
        countryTempsRange.append(diff)      
    print(countryTempsRange)
    print(diffList)

    newListOfCountry = [] 
    counter = 0
    for cou in listOfCountry:
        newListOfCountry.append(f'{cou} {diffList[counter]}')
        counter += 1

    explodeTuple = tuple(explodeList)       
    plt.title(f'Difference of Yearly Mean Temperature {yearRangeFrom} to {yearRangeTo}')
    plt.pie(countryTempsRange, labels=newListOfCountry, autopct='%1.1f%%', explode=explodeTuple, shadow=True, startangle=90, labeldistance=.9, pctdistance=0.5)
    plt.text(1.2, 0, 'Exploded means negative values', fontsize=8, verticalalignment='center', bbox=dict(facecolor='lightgray', alpha=0.5))
    plt.tight_layout()
    plt.show()

print('Welcome, this program has 3 functions')
print('Function 1 (Line graph): Find out the monthly mean temperatures of a certain country within a certain year')
print('Function 2 (Bar chart): Find out the yearly mean temperatures of multiple countries within a year range')
print('Function 3 (Pie chart): Find out the the percentage of change of yearly mean temperature of 2 selected years compared to other countries')

while True:
    try:
        command = int(input('Please type 1, 2, 3 for Function 1, 2, 3: '))
        if command == 1:
            function1()
        elif command == 2:
            function2()
        elif command == 3:
            function3()
        else:
            print('Error: Please type in a number between 1-3 inclusive')
    except ValueError:
        print('Error: Please type in a numeric value between 1-3 inclusive')

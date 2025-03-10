#Coursework Computational Artefact // Collecting and Preparing Data
import pandas as pd

#Extracting my dataframe
file_path = 'dirtyDF.csv'
dataIn = pd.read_csv(file_path)
print(dataIn.head(10))

#Removing Celsius Symbol
dataIn['AverageTemperature'] = dataIn['AverageTemperature'].replace({'°C':''}, regex=True)
print('\n\n\nAFTER REMOVING C\n', dataIn.head(10))

#Changing relevant columns to numeric value
dataIn['AverageTemperature'] = pd.to_numeric(dataIn['AverageTemperature'], errors='coerce')
dataIn['AverageTemperatureUncertainty'] = pd.to_numeric(dataIn['AverageTemperatureUncertainty'], errors='coerce')

#Remove duplicate rows
dataIn = dataIn.drop_duplicates()

#Remove rows with empty AverageTemperature
dataIn = dataIn[dataIn['AverageTemperature'].notna()]
print('\n\n\nAFTER REMOVING EMPTY AVERAGE TEMP ROWS\n',dataIn.head(10))

#Before 1900, format is in YYYY-MM-DD.  1900 and after, format is DD/MM/YYYY
#Converting all dt cell from DD/MM/YYYY to YYYY-MM-DD format, (Only 1900 and after will be carried over)
dataIn['dt'] = pd.to_datetime(dataIn['dt'], format='%d/%m/%Y', errors='coerce')
print('\n\n\nAFTER CONVERTING 1900 AND AFTER\n',dataIn.head(10))

#Removing all those cells that are not converted to YYYY-MM-DD format (Before 1900 cells, who are converted from YYYY-MM-DD to NaT)
dataIn = dataIn[dataIn['dt'].notna()]
print('\n\n\nAFTER REMOVING BEFORE 1900\n',dataIn.head(10))

#Removing those that are before 2000
dataIn = dataIn.loc[(dataIn['dt'] >= '2000-01-01')]
print('\n\n\nFINAL RESULT\n',dataIn.head(10))

dataIn.to_csv('cleanedDF.csv', index=False)










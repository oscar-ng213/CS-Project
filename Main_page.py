import streamlit as st

st.title('Homepage')

st.markdown('Welcome')
st.write('Function 1 (Line graph): Find out the yearly mean temperatures of multiple countries within a year range')
st.write('Function 2 (Bar chart): Find out the monthly mean temperature of a country in a year')
st.write('Function 3 (Pie chart): Find out the percentage of change of yearly mean temperature compared against multiple countries')
st.write('Function 4 (Linear Regression): Take the values from the dataframe calculate line of best fit, and checking out if the slope is warming faster than average or not.')



st.sidebar.success("Select a function above.")
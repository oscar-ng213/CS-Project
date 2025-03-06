import streamlit as st

st.title('Homapage')

st.markdown('Welcome, this program has 4 functions')
st.write('Function 1 (Line graph): Find out the monthly mean temperatures of a certain country within a certain year')
st.write('Function 2 (Bar chart): Find out the yearly mean temperatures of multiple countries within a year range')
st.write('Function 3 (Pie chart): Find out the the percentage of change of yearly mean temperature of 2 selected years compared to multiple countries')
st.write('Function 4 (Linear Regression): Take the values from the dataframe calculate line of best fit, and checking out if the slope is warming faster than average or not.')

st.sidebar.success("Select a function above.")
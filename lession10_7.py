import streamlit as st
import datetime

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)


number = st.number_input('Insert a number')
st.write('The current number is ', number)


d = st.date_input(
    "When\'s your birthday",
    datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)
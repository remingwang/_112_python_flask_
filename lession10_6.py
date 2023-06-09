import streamlit as st

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)
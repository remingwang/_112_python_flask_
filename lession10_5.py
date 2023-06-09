import streamlit as st

options = st.multiselect(
    '請選擇您喜歡的顏色',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('您選擇:', options)
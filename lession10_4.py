import streamlit as st

option = st.selectbox(
    '您想要如何聯絡?',
    ('Email', '電話', '手機'))

st.write('You selected:', option)
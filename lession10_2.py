import streamlit as st

agree = st.checkbox('我同義')

if agree:
    st.write('Great!')
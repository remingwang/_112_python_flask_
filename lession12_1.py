import streamlit as st
import pandas as pd

codeFrame = pd.read_csv('codeSearch.csv',usecols=['code','name'])
codeSeries = codeFrame['code'].astype(str) + codeFrame['name'] 



with st.sidebar:
    st.multiselect("請選擇股票號碼:",codeSeries)

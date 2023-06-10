import streamlit as st
import pandas as pd
import yfinance as yf

codeFrame = pd.read_csv('codeSearch.csv',usecols=['code','name'])
codeSeries = codeFrame['code'].astype(str) + codeFrame['name'] 



with st.sidebar:
   selected_codes =  st.multiselect("請選擇股票號碼:",codeSeries,
                                    max_selections = 4)
   
@st.cache_data
def fetch_stock_daraFram(id):
   stock_daraFram= yf.download('2330.TW',start='2022-01-01')
   return stock_daraFram
for code in selected_codes:
   code1 = code[:4]+".TW"
   code_stock_dataFram = fetch_stock_daraFram(code1)
   code_stock_dataFram_sorted= code_stock_dataFram.sort_index(ascending=False)
   st.subheader(code)
   st.dataframe(code_stock_dataFram_sorted,width=1024)
   st.line_chart(code_stock_dataFram_sorted,y='Adj Close')
   st.divider()

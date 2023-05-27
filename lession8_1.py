import requests
import pandas as pd
import streamlit as st
url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
respones = requests.request('GET',url)
if respones.status_code == 200:
    print("連線成功")
    all_data = respones.json()
    print(type(all_data))
    
else:
    print(f"連線失敗:{respones.status_code}")

dataFrame = pd.DataFrame(data=all_data,columns=['sna','tot','sbi','sarea','mday','ar','bemp','act'])
#dataFrame.info()
#min = int(input("請輸入要查詢的可借數量"))
#mask = dataFrame['sbi'] <= min
mask = dataFrame['sbi'] <=3
mask_datafram = dataFrame[mask]
st.dataframe(mask_datafram)
#filename = f'可借數量小於{min}的站點.xlsx'
#mask_datafram.to_excel(filename)
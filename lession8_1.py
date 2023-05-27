import requests
import pandas as pd
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
mask = dataFrame['sbi'] <=3
mask_datafram = dataFrame[mask]
mask_datafram.to_excel('可借小於3.xlsx')
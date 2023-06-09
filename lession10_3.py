import streamlit as st

genre = st.radio(
    "您喜歡的節目是什麼",
    ('卡通', '戲劇', '愛情'))

if genre == '卡通':
    st.write('您選擇:卡通')
elif genre == "戲劇" :
    st.write("您選擇:戲劇")
elif genre == '愛情':
    st.write("您選擇:愛情")
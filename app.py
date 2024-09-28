import streamlit as st
import matplotlib.pyplot as plt

# 設定標題
st.title("Test")

# 準備資料
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

# 繪製長條圖
plt.bar(categories, values, color='skyblue')
plt.xlabel('category')
plt.ylabel('value')
plt.title('test')

# 在 Streamlit 中顯示圖表
st.pyplot(plt)

# 顯示數據
st.write("data:")
st.write({"categories": categories, "values": values})
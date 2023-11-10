import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Reference Index", page_icon=":key:", layout="wide")
st.title('Self evaluate your homestay level!')
st.write("📍Do you want to know where your house's different indices are located in the city?")
st.write("👉Here are the average, maximum, and minimum values of different indices for different cities. ")
st.write("👀By comparing the index of one's own house with the average, maximum, and minimum values on this image, the host can find the location of different indices of one's own house for better improvement.")

# 读取数据
df = pd.read_csv('Aemf1.csv')

# 按城市分组计算均值、最大值和最小值
df_by_city = df.groupby('City')
mean = df_by_city[['Guest Satisfaction']].mean()
mean['max'] = df_by_city[['Guest Satisfaction']].max()
mean['min'] = df_by_city[['Guest Satisfaction']].min()

# Streamlit 应用
st.sidebar.header("Please filter:")
selected_metric = st.sidebar.radio('choose your index', ['Guest Satisfaction', 'Cleanliness Rating', 'Attraction Index', 'Restraunt Index'])

# 更新图表
fig, ax = plt.subplots()

# 根据用户选择的指标更新数据
if selected_metric == 'Guest Satisfaction':
    mean = df_by_city[['Guest Satisfaction']].mean()
    mean['max'] = df_by_city[['Guest Satisfaction']].max()
    mean['min'] = df_by_city[['Guest Satisfaction']].min()
elif selected_metric == 'Cleanliness Rating':
    mean = df_by_city[['Cleanliness Rating']].mean()
    mean['max'] = df_by_city[['Cleanliness Rating']].max()
    mean['min'] = df_by_city[['Cleanliness Rating']].min()
elif selected_metric == 'Attraction Index':
    mean = df_by_city[['Attraction Index']].mean()
    mean['max'] = df_by_city[['Attraction Index']].max()
    mean['min'] = df_by_city[['Attraction Index']].min()
elif selected_metric == 'Restraunt Index':
    mean = df_by_city[['Restraunt Index']].mean()
    mean['max'] = df_by_city[['Restraunt Index']].max()
    mean['min'] = df_by_city[['Restraunt Index']].min()

# 绘制图表
mean.plot(ax=ax)
plt.xlabel('City')
plt.xticks(rotation=45)

# 显示图表
st.pyplot(fig)

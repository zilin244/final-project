import streamlit as st

# 设置页面标题和图标
st.set_page_config(page_title="Airbnb Europe Dataset", page_icon=":house:")

# 设置动画
st.balloons()

# 创建一个Streamlit应用
st.title("👋Welcome to Airbnb Europe Dataset!")

# 添加标题动画效果
st.markdown(
    """
    Airbnb Europe Dataset is an app which provides a detailed analysis of the data about residential hostels of 9 famous cities in Europe. 
    - Source: The source of data is from the Kaggle website
    
    (https://www.kaggle.com/datasets/dipeshkhemani/airbnb-cleaned-europe-dataset).
    - Target user: The target users of this app is customers and hosts. 
    - Function: The app not only aims to help customers learn about folklore market situation of this city they want to go and make decisions validly, 
    but also help hosts understand their own strengths and weaknesses and make improvements.

    ##### 👈 You can chosee a page in the siderbar!

    ### For customers:
    - Find the determinants of Airbnb prices in European cities after reading **[Correlation Analysis of Price]**
    - Learn about the average price per person in **[Price]**
    - Popular room types in different regions in **[Room Type]**
    - The level of homestay services in different cities in **[Service]**
    ### For hosts:
    - page1
    - page2
"""
)

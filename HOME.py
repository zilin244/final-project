import streamlit as st

st.set_page_config(page_title="Airbnb Europe Dataset", page_icon=":house:")


st.balloons()


st.title("👋Welcome to Airbnb Europe Dataset!")


st.markdown(
    """
    Airbnb Europe Dataset is an app which provides a detailed analysis of the data about residential hostels of 9 famous cities in Europe. 
    - Source: The source of data is from the Kaggle website
    
    (https://www.kaggle.com/datasets/dipeshkhemani/airbnb-cleaned-europe-dataset)
    - Target user: The target users of this app is customers and hosts. 
    - Function: The app not only aims to help customers learn about folklore market situation of this city they want to go and make decisions validly, 
    but also help hosts understand their own strengths and weaknesses and make improvements.

    ##### 👈 You can chosee a page in the siderbar!

    ### For customers:
    - Help you make decisions in Price **[Price]**
    - Popular room types in different regions in **[Room Type]**
    - The level of homestay services in different cities in **[Service]**
    ### For hosts:
    - Learn about the correlation between Attraction Index and other variables in **[Attraction index]**
    - Distance vs Attraction Index in **[Distance]**
    - Evaluate your homestay level in **[Reference Index]**
"""
)

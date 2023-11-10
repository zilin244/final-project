import pandas as pd
import streamlit as st
import numpy as py
import altair as al
import matplotlib.pyplot as plt

def get_data():
    d = pd.read_csv("Aemf1.csv") 
    return d

df = get_data()

st.set_page_config(page_title="Room Type", page_icon=":key:", layout="wide")
st.title(":piechart: Popular Room Types in Different Cities")
st.markdown("""
There are different popular room types in different places. People often want to experience a popular local room type as a special experience. 
**This page analyzes the number and proportion of room types in different cities.**

What are the popular housing types in your target city?

- The bar chart shows the total number of room types in different cities on Airbnb.

""")

df_by = df.groupby(['City','Room Type'])
table_count = df_by[['Price']].count()
table_c = pd.pivot_table(data=table_count,
                   values = "Price",
                   index = "City",
                   columns = 'Room Type')

plt.style.use("seaborn-v0_8")

ax = table_c.plot(kind="bar")

# plt.figure(figsize=(30,30))
# plt.legend(loc='upper right')
ax.set_xlabel("City", fontsize = 15)
ax.set_ylabel("Count", fontsize = 15)
# ax.set_ylim(0,6000)

st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

st.markdown("""

- The pie chart gives you a more intuitive sense of the proportion of different room types in the city.


""")
city = df['City'].unique()
c = st.text_input('Enter the city you want to search for: ', value='Amsterdam', key=None)
city = str(c)
table_p = pd.pivot_table(data=table_count,
                   values = "Price",
                   index = "Room Type",
                   columns = 'City')
labels=df['Room Type'].unique()
p = table_p[city]
plt.pie(p,autopct='%0.2f%%',labels=labels,shadow=True)

st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

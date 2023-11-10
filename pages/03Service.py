import pandas as pd
import streamlit as st
import numpy as py
import altair as al
import matplotlib.pyplot as plt
import seaborn as sns

## read the data
def get_data():
    d = pd.read_csv("Aemf1.csv") 
    return d

df = get_data()

st.set_page_config(page_title="Average price per person", page_icon=":bar_chart:", layout="wide")

st.title(":smile: Service")
st.markdown("### In this page, the level of serive across different city is persented. ")

df_at=df.copy()

fig, ax = plt.subplots()

df_at[df_at['Cleanliness Rating']>6].boxplot(column=['Cleanliness Rating'],by = ['City'],ax=ax,meanline=True,showmeans=True);

fig.suptitle("")
plt.xticks(rotation=60)
## Now we can actually set the Title
plt.title("Cleanliness Rating by Different City")

st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(fig)


fig, ax = plt.subplots()

df_at[df_at['Normalised Restraunt Index']<100].boxplot(column=['Normalised Restraunt Index'],by = ['City'],ax=ax,meanline=True,showmeans=True);

fig.suptitle("")
plt.xticks(rotation=60)
## Now we can actually set the Title
plt.title("Normalised Restraunt Index by Different City")

st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

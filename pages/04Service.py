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


fig, ax = plt.subplots()

df[df['Price']<2000].boxplot(column=['Price'],by = ['City'],ax=ax,meanline=True,showmeans=True);

fig.suptitle("")
plt.xticks(rotation=60)
## Now we can actually set the Title
plt.title("Price by Different City")

df1=df[['Cleanliness Rating','Superhost','Metro Distance (km)','Normalised Restraunt Index']]

l = df1.columns.values ## List of the variables from the columns
number_of_columns= len(l) ## For the plot
number_of_rows = 1 ## For the plot

plt.subplots(figsize=(2*number_of_columns,10*number_of_rows))
for i in range(0, number_of_columns):
    plt.subplot(number_of_rows + 1,number_of_columns,i+1)
    plt.title(l[i])
    plt.style.use("seaborn-v0_8")
    sns.boxplot(df1[l[i]],color='green',orient='v')
    plt.tight_layout();
plt.ylim(0.5,1.0)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(fig)

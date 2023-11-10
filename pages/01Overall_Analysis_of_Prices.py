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

st.set_page_config(page_title="Correlation Analysis of Price", page_icon=":chart:", layout="wide")

st.title(":chart: Correlation Analysis of Price")

st.markdown(""" 
            #####  This page focus on **the analysis of price**. In this page, you can learn about the correlation between prices and other variables in European Airbnb and further analysis of the price.
             
1. Here's a heatmap about price and its top variables that are the most correlated in absolute value
  """)

plt.style.use("seaborn-v0_8")

dfm=df.copy()
#Map Neighbourhood and Room Type to numeric encoding
City = {'Amsterdam': 0, 'Athens': 1, 'Barcelona': 2, 'Berlin': 3, 'Budapest': 4,'Lisbon':5,'Paris':6,'Rome':7,'Vienna':8}
room_type= {'Entire home/apt': 0, 'Private room': 1,'Shared Room':2}
day = {'Weekday':0,'Weekend':1}
dfm['Price'] = df['Price'].apply(lambda x: float(str(x).replace(',', '')))
dfm['City'] = df['City'].map(City)
dfm['Room Type'] = df['Room Type'].map(room_type)
dfm['Day']=df['Day'].map(day)
#Select the columns to analyze
df_num = dfm[['Person Capacity', 'City', 'Day', 'Room Type', 'Superhost', 'Business', 'Cleanliness Rating', 'Guest Satisfaction', 'Price', 'City Center (km)']]
#Calculate correlation matrix
k = 8 
#Set the number of data with the highest correlation to list
cols = df_num.corr().abs().nlargest(k + 1, 'Price')['Price'].index
cm = df_num[cols].corr()
#Draw a heat map
fig, ax = plt.subplots()
plt.figure(figsize=(15, 9))
ax = sns.heatmap(cm, annot=True, cmap='Blues')
plt.title('top 8 variables that are the most correlated /n in absolute value with the Price ')

st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

st.markdown(""" 
            There is a stronger correlation between price and three features which are person capacity, room type and guest satisfication.
  """)

st.markdown(""" 
2. This is a boxplot about price analysis in different city. 
This chart helps customers compare the various special values of accommodation prices in different cities longitudinally.
You can clearly find the mean value, median and extreme value in the figrue """)

fig, ax = plt.subplots()

df[df['Price']<2000].boxplot(column=['Price'],by = ['City'],ax=ax,meanline=True,showmeans=True);

fig.suptitle("")
plt.xticks(rotation=60)
## Now we can actually set the Title
plt.title("Price by Different City")


st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

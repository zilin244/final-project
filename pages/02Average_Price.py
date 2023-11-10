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


# 侧边栏
st.sidebar.header("Please filter:")
city = st.sidebar.radio(
    "City:",
    df["City"].unique()
)

superhost = st.sidebar.radio(
    "Superhost:",
    df["Superhost"].unique()
)

business = st.sidebar.radio(
    "Business:",
    df["Business"].unique()
)

person = st.sidebar.radio(
    "Person Capacity:",
    df["Person Capacity"].sort_values().unique()
)

df_selection = df[(df['City']==city) & (df['Person Capacity']==person) & (df['Business']==business) & (df['Superhost']==superhost)]

# 主页面
st.title(":bar_chart: Average Price")
st.markdown(""" **This page preshents the average price per person across different room type.**

If you want to select a residential hostel with friends or family, which room types is the best deal? Are prices cheaper on weekdays than on weekends?

- Step1: Select what you want in the sidebar
- Step2: Barchart will give you some information.You can clearly find the lowest bar in the figure.
""")
# 画图

table = df_selection.groupby(['Person Capacity','Room Type','Day'])
mean_price = table[['Price']].mean()

list1 = mean_price.Price.tolist()
# num_person = table['Person Capacity'].unique().tolist()
list_averfare = []
num_p = int(person)
for i in range(len(list1)):
    # value = list1[i] / num_person[i]
    value = list1[i] / num_p
    list_averfare.append(value)
mean_price['Average Price Per Person'] = list_averfare
table_mean = pd.pivot_table(data=mean_price,
                   values = "Average Price Per Person",
                   index = "Room Type",
                   columns = 'Day')

st.set_option('deprecation.showPyplotGlobalUse', False)

plt.style.use("seaborn-v0_8")
ax1 = table_mean.plot(kind='bar')
ax1.set_ylabel('Average Fare Per Person')
ax1.set_title('Average Price Per Person across Room Type')

st.pyplot()


            
st.markdown(""" 
This is a boxplot about price analysis in different city. 
This chart helps customers compare the various special values of accommodation prices in different cities longitudinally.
  """)

fig, ax = plt.subplots()

df[df['Price']<2000].boxplot(column=['Price'],by = ['City'],ax=ax,meanline=True,showmeans=True);


plt.xticks(rotation=60)
## Now we can actually set the Title
plt.title("Price by Different City")


st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()


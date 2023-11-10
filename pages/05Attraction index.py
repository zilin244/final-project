import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title(":star: Correlation of Attraction Index")

# read the dataset file
df = pd.read_csv('Aemf1.csv')
df_t_num = df[['Attraction Index','Price','Person Capacity','Superhost','Multiple Rooms','Business','Cleanliness Rating','Guest Satisfaction','Bedrooms','City Center (km)','Metro Distance (km)','Restraunt Index']]

#Quality correlation matrix
k = 11 #number of variables for heatmap
## Get the k most correlated in absolute value
cols = df_t_num.corr().abs().nlargest(k+1, 'Attraction Index')['Attraction Index'].index
cm = df_t_num[cols].corr()

# create the heatmap
fig, ax = plt.subplots(figsize=(15,8))
sns.heatmap(cm, annot=True, cmap = 'Blues')
ax.set_title('Quality Correlation Matrix')


# show on streamlit
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot(fig)

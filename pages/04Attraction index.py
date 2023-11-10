import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title(":star: Correlation of Attraction Index")
st.markdown("""   **This page focus on the analysis of Attraction Index.** 
In this page, you can learn about the correlation between Attraction Index and other variables in European Airbnb and further analysis of the Attraction Index.

 Here's a heatmap about Attraction Index and its top variables that are the most correlated in absolute value """)
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
st.markdown(""" From the heatmap, we can see that the variable with a high correlation with the Attraction Index is Restraunt Index, City Center(km), Price and Metro Distance(km), where Restraunt Index and Price are positively correlated, and City Center (km) and Metro Distance(km) are negatively correlated.

That is to say, to improve the Attraction Index, the host can increase the Restraunt Index and Price, reduce City Center (km) and Metro Distance(km). What's more, the correlation between other variables and Attraction Index is very low, we can ignore their impact on Attraction Index.

To learn more about the impact of distance on attractiveness index, please refer to the next page.  """)

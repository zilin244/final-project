import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Distance", page_icon=":railway_car:", layout="wide")
st.title("City Center vs Attraction Index")
st.write("👉You can look at the relationship between ") 
st.write("👉Attraction Index and distance between homestays and city center") 

# read the dataset file
df = pd.read_csv('Aemf1.csv')

# Create Scatter Chart
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(df['City Center (km)'], df['Attraction Index'], label='Data Points', color='blue', marker='o')
ax.set_xlabel('City Center (km)')
ax.set_ylabel('Attraction Index')
ax.set_title('City Center vs Attraction Index')
ax.grid(True)
ax.legend()

# Create a slider to control the x-axis range
x_min, x_max = st.slider('choose a range ', 0.0, 25.0, (0.0, 25.0))

# Filter data based on slider values
df_filtered = df[(df['City Center (km)'] >= x_min) & (df['City Center (km)'] <= x_max)]

# Create filtered scatter plots
fig_filtered, ax_filtered = plt.subplots(figsize=(8, 6))
ax_filtered.scatter(df_filtered['City Center (km)'], df_filtered['Attraction Index'], label='Data Points', color='blue', marker='o')
ax_filtered.set_xlabel('City Center (km)')
ax_filtered.set_ylabel('Attraction Index')
ax_filtered.set_title('City Center vs Attraction Index (Filtered)')
ax_filtered.grid(True)
ax_filtered.legend()

# show on streamlit
st.pyplot(fig_filtered)


st.title("Metro Distance vs Attraction Index")
st.write("👉You can look at the relationship between ") 
st.write("👉Attraction Index and distance between homestays and metro station") 
# read the dataset file
df = pd.read_csv('Aemf1.csv')

# Create Scatter Chart
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(df['Metro Distance (km)'], df['Attraction Index'], label='Data Points', color='blue', marker='o')
ax.set_xlabel('Metro Distance (km)')
ax.set_ylabel('Attraction Index')
ax.set_title('Metro Distance vs Attraction Index')
ax.grid(True)
ax.legend()

# Create a slider to control the x-axis range
x_min, x_max = st.slider('choose a range ', 0.0, 15.0, (0.0, 15.0))

# Filter data based on slider values
df_filtered = df[(df['Metro Distance (km)'] >= x_min) & (df['Metro Distance (km)'] <= x_max)]

# Create filtered scatter plots
fig_filtered, ax_filtered = plt.subplots(figsize=(8, 6))
ax_filtered.scatter(df_filtered['Metro Distance (km)'], df_filtered['Attraction Index'], label='Data Points', color='blue', marker='o')
ax_filtered.set_xlabel('Metro Distance (km)')
ax_filtered.set_ylabel('Attraction Index')
ax_filtered.set_title('Metro Distance vs Attraction Index (Filtered)')
ax_filtered.grid(True)
ax_filtered.legend()

# show on streamlit
st.pyplot(fig_filtered)
st.markdown(""" Based on the Scatter plot, we can find that: 
there is a certain negative correlation between the Attraction index and the distance of the city center.

As we pull the button, the chart can more intuitively display the relationship between the two, 
in order to provide a better solution """)

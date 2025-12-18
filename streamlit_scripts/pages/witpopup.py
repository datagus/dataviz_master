import pandas as pd
import folium
import streamlit as st
from folium.plugins import FastMarkerCluster
from streamlit_folium import st_folium


st.write("# Welcome to this awesome map with FOLIUM")

df = st.session_state.data.copy()

df_good = df.loc[~df["latitude"].isna(),]

# create a clean list of options of state names
states = df_good["state"].unique().tolist()

option = st.sidebar.selectbox(
    "Which state would you like to see",
    states
)

filtered_df = df_good.copy()


filtered_df = filtered_df.loc[filtered_df["state"]==option,]

m = folium.Map(location=[filtered_df['latitude'].mean(), filtered_df['longitude'].mean()], zoom_start=8)

for _, row in filtered_df.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        popup=f"$ {row["price"]}",
        radius=4,
        fill=True
    ).add_to(m)

st_data = st_folium(m, width=725)




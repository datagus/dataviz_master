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
states.insert(0, "All states")   # put "All states" at the top

option = st.sidebar.selectbox(
    "Which state would you like to see",
    states
)

filtered_df = df_good.copy()

if option=="All states":
	
	m = folium.Map(location=[df_good['latitude'].mean(), df_good['longitude'].mean()], zoom_start=7)
	
	# Create list of [lat, lon] coordinates
	coordinates = df_good[['latitude', 'longitude']].values.tolist()
	
	# Add all markers at once
	FastMarkerCluster(coordinates).add_to(m)
	
	st_data = st_folium(m, width=725)

	
	
else:
	
	filtered_df = filtered_df.loc[filtered_df["state"]==option, ]
	
	m = folium.Map(location=[filtered_df['latitude'].mean(), filtered_df['longitude'].mean()], zoom_start=7)
	
	# Create list of [lat, lon] coordinates
	coordinates = filtered_df[['latitude', 'longitude']].values.tolist()
	
	# Add all markers at once
	FastMarkerCluster(coordinates).add_to(m)
	
	st_data = st_folium(m, width=725)





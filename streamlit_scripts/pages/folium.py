import pandas as pd
import folium
import streamlit as st
from folium.plugins import FastMarkerCluster
from streamlit_folium import st_folium


st.write("# Welcome to this awesome map with FOLIUM")

df = st.session_state.data.copy()

df_good = df.loc[~df["latitude"].isna(),]


state_full_names = {
    "DC": "District of Columbia",
    "IN": "Indiana",
    "VA": "Virginia",
    "WA": "Washington",
    "NY": "New York",
    "CA": "California",
    "AZ": "Arizona",
    "NC": "North Carolina",
    "TX": "Texas",
    "GA": "Georgia",
    "FL": "Florida",
    "AL": "Alabama",
    "MD": "Maryland",
    "CO": "Colorado",
    "NM": "New Mexico",
    "IL": "Illinois",
    "TN": "Tennessee",
    "AK": "Alaska",
    "MA": "Massachusetts",
    "NJ": "New Jersey",
    "OR": "Oregon",
    "DE": "Delaware",
    "PA": "Pennsylvania",
    "IA": "Iowa",
    "SC": "South Carolina",
    "MN": "Minnesota",
    "MI": "Michigan",
    "KY": "Kentucky",
    "WI": "Wisconsin",
    "OH": "Ohio",
    "CT": "Connecticut",
    "RI": "Rhode Island",
    "NV": "Nevada",
    "UT": "Utah",
    "MO": "Missouri",
    "OK": "Oklahoma",
    "NH": "New Hampshire",
    "NE": "Nebraska",
    "LA": "Louisiana",
    "ND": "North Dakota",
    "AR": "Arkansas",
    "KS": "Kansas",
    "ID": "Idaho",
    "HI": "Hawaii",
    "MT": "Montana",
    "VT": "Vermont",
    "SD": "South Dakota",
    "WV": "West Virginia",
    "MS": "Mississippi",
    "ME": "Maine",
    "WY": "Wyoming"
}

# Second, use the method.map() to get the full names and creating a new column
df_good["state_full"] = df_good["state"].map(state_full_names)

# create a clean list of options of state names
states = df_good["state_full"].unique().tolist()
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
	
	filtered_df = filtered_df.loc[filtered_df["state_full"]==option, ]
	
	m = folium.Map(location=[filtered_df['latitude'].mean(), filtered_df['longitude'].mean()], zoom_start=7)
	
	# Create list of [lat, lon] coordinates
	coordinates = filtered_df[['latitude', 'longitude']].values.tolist()
	
	# Add all markers at once
	FastMarkerCluster(coordinates).add_to(m)
	
	st_data = st_folium(m, width=725)





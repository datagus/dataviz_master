import streamlit as st
import pandas as pd

st.title("Check my awesome map")

df = st.session_state.data.copy()

df = df.loc[~df["latitude"].isna(),]


# create a clean list of options of state names
states = df["state"].unique().tolist()
states.insert(0, "All states")   # put "All states" at the top

option = st.sidebar.selectbox(
    "Which state would you like to see",
    states
)

filtered_df = df.copy()

if option=="All states":
	
	st.map(data=df, latitude = "latitude", longitude="longitude", color="#ffaa00", zoom=2)
	
else:
	filtered_df = filtered_df.loc[filtered_df["state"]==option, ]
	st.map(data=filtered_df, latitude = "latitude", longitude="longitude")
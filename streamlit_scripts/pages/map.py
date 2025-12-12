import streamlit as st
import pandas as pd

st.title("Check my awesome map")

df = st.session_state.data.copy()

df = df.loc[~df["latitude"].isna(),]


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
df["state_full"] = df["state"].map(state_full_names)

# create a clean list of options of state names
states = df["state_full"].unique().tolist()
states.insert(0, "All states")   # put "All states" at the top

option = st.sidebar.selectbox(
    "Which state would you like to see",
    states
)

filtered_df = df.copy()

if option=="All states":
	
	st.map(data=df, latitude = "latitude", longitude="longitude", color="#ffaa00", zoom=2)
	
else:
	filtered_df = filtered_df.loc[filtered_df["state_full"]==option, ]
	st.map(data=filtered_df, latitude = "latitude", longitude="longitude")
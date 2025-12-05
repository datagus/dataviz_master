import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#you can use streamlit functions by always starting with st.


#Adding a title that always show at the top of your app
st.title("Rent Aparments in USA - Dashboard")

#you can import a dataframe from an external source
base_url = "https://docs.google.com/spreadsheets/d/"
url_id = "1NV-k5237esNE6lugwYw4hZVoRcYi8SFtG4fzX3aokAo/"
export = "export/format=excel"
whole_url = base_url + url_id + export

#however, to avoid reloading everytime your script runs, you need to a cache
@st.cache_data()   
def load_data(): #use a function most of the time to import data in streamlit
    df = pd.read_excel(whole_url, na_values="None")
    return df
	
#now you can import your data
df = load_data()  


#the function st.sidebar gives you a side bar in your app, you can add whatever you want.
# For example, you can add an expander in the side bar to hide/show the dataset description:
with st.sidebar.expander("Dataset description"):
    st.write("""The dataset contains of 10'000 or 100'000 rows and of 22 columns The data has been cleaned in the way that 
column price and square_feet never is empty but the dataset is saved as it was created.

Can be used for different machine learning tasks such as clustering, classification and also regression for the squares feet column""")

dataset_description = {
    "id": "unique identifier of the apartment",
    "category": "category of the classified",
    "title": "title text of the apartment",
    "body": "body text of the apartment",
    "amenities": "list of amenities (AC, basketball, cable, gym, internet access, pool, refrigerator, etc.)",
    "bathrooms": "number of bathrooms",
    "bedrooms": "number of bedrooms",
    "currency": "price currency",
    "fee": "fee information",
    "has_photo": "indicates whether the apartment has a photo",
    "pets_allowed": "types of pets allowed (dogs, cats, etc.)",
    "price": "rental price of the apartment",
    "price_display": "price formatted for display",
    "price_type": "price in USD",
    "square_feet": "size of the apartment",
    "address": "address of the apartment",
    "cityname": "city where the apartment is located",
    "state": "state where the apartment is located",
    "latitude": "geographic latitude",
    "longitude": "geographic longitude",
    "source": "origin of the classified",
    "time": "timestamp of when the classified was created"
}

# sidebar selectbox to see the description of variables
variable_names = df.columns.tolist()

selected_var = st.sidebar.selectbox(
    "Check the variable description",
    df.columns.tolist()
)

with st.sidebar:
    description = dataset_description.get(selected_var)

    st.markdown(
        f"""
        <div style="
            background-color:white;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #DDD;
            color: black;">
            {description}
        </div>
        """,
        unsafe_allow_html=True
    )

# Let's subselect a dataframe according to the state we want

# First, we need to create a dictionary of states abbreviations with the full names

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
	st.dataframe(df)
else:
	filtered_df = filtered_df.loc[filtered_df["state_full"]==option, ]
	apart_count = filtered_df["id"].nunique()
	st.info(f"There are {apart_count} apartments in {option}")
	st.dataframe(filtered_df)
	
########

# create a clean list of options of cities
cities = filtered_df["cityname"].unique().tolist()
#states.insert(0, "All states")   # put "All states" at the top

option2 = st.sidebar.selectbox(
    "Which city would you like to see",
    cities
)
city_df = df.loc[df["cityname"]==option2]

#creating countplot
st.title(f"Pets allowed in {option2}")

# Create the figure
fig, ax = plt.subplots(figsize=(12, 6))
sns.countplot(data=city_df, x="pets_allowed")

ax.set_xlabel("Pets")
ax.set_ylabel("Count")
plt.xticks(rotation=45)

# Show it in Streamlit
st.pyplot(fig)

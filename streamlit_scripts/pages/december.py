import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.title("This is my page with tabs")

df = st.session_state.data.copy()

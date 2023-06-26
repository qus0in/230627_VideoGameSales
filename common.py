import streamlit as st
import pandas as pd

@st.cache_data
def get_sales():
    return pd.read_csv("./vgsales.csv")
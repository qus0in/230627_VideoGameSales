import streamlit as st
import pandas as pd

@st.cache_data
def get_sales():
    return pd.read_csv("./vgsales.csv")

def page_config():
    st.set_page_config(
        page_title="Video Game Sales",
        page_icon="🎮",
    )
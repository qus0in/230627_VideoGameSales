import streamlit as st
import common

st.title("Data")
st.dataframe(common.get_sales(),
             use_container_with=True)

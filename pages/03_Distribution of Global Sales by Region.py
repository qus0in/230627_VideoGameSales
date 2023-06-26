import matplotlib.pyplot as plt
import streamlit as st
import plotly.graph_objects as go
import common

common.page_config()

st.title("Distribution of Global Sales by Region")

df = common.get_sales()

region_sales = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()

tab1, tab2 = st.tabs(["Pyplot", "Plotly"])

with tab1:
    plt.pie(region_sales, labels=region_sales.index, autopct='%1.1f%%')
    plt.title('Distribution of Global Sales by Region')
    st.pyplot(plt)

with tab2:
    fig = go.Figure(data=[go.Pie(labels=region_sales.index, values=region_sales.values, hole=0.3)])
    fig.update_layout(
        title='Distribution of Global Sales by Region',
    )
    st.plotly_chart(fig,
                    use_container_width=True)
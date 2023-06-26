import matplotlib.pyplot as plt
import streamlit as st
import plotly.graph_objects as go
import common

st.title("Bar Graph")

df = common.get_sales()

region_sales = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()

tab1, tab2 = st.tabs(["Pyplot", "Plotly"])

with tab1:
    plt.pie(region_sales, labels=region_sales.index, autopct='%1.1f%%')
    plt.title('Distribution of Global Sales by Region')
    st.pyplot(plt)

with tab2:
    pass
    # fig = go.Figure(data=[go.Bar(x=genre_counts.index, y=genre_counts.values)])
    # fig.update_layout(
    #     xaxis=dict(
    #         title='Genre',
    #         tickangle=90,
    #     ),
    #     yaxis=dict(
    #         title='Number of Games',
    #     ),
    #     title='Number of Video Games by Genre',
    # )
    # st.plotly_chart(fig)
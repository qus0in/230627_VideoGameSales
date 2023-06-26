import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import common

common.page_config()

st.title("Distribution of Global Sales by Genre")

df = common.get_sales()

genre_sales = df.groupby('Genre')['Global_Sales'].sum()

tab1, tab2 = st.tabs(["Pyplot", "Plotly"])

with tab1:
    plt.pie(genre_sales, labels=genre_sales.index, autopct='%1.1f%%')
    plt.title('Distribution of Global Sales by Genre')
    st.pyplot(plt)

with tab2:
    fig = go.Figure(data=[go.Pie(labels=genre_sales.index, values=genre_sales.values, hole=0.3)])
    fig.update_layout(
        title='Distribution of Global Sales by Genre',
    )
    st.plotly_chart(fig,
                    use_container_width=True)
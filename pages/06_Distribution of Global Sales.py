import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import common

common.page_config()

st.title("Global Sales by Year and Genre")

df = common.get_sales()

year_sales = df.groupby('Year')['Global_Sales'].sum()

tab1, tab2 = st.tabs(["Pyplot", "Plotly"])

with tab1:
    plt.plot(year_sales.index, year_sales.values)
    plt.xlabel('Year')
    plt.ylabel('Global Sales (in millions)')
    plt.title('Global Sales by Year')
    st.pyplot(plt)

with tab2:
    fig = go.Figure(data=go.Scatter(
        x=year_sales.index,
        y=year_sales.values,
        mode='lines',
    ))
    fig.update_layout(
        title='Global Sales by Year',
        xaxis=dict(title='Year'),
        yaxis=dict(title='Global Sales (in millions)'),
    )
    st.plotly_chart(fig,
                    use_container_width=True)
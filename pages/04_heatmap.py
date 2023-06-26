import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import common

st.title("Heatmap")

df = common.get_sales()

sales_by_year_genre = df.pivot_table(index='Genre', columns='Year', values='Global_Sales', aggfunc='sum')

tab1, tab2 = st.tabs(["Seaborn", "Plotly"])

with tab1:
    plt.figure(figsize=(12, 6))
    sns.heatmap(sales_by_year_genre, cmap='YlGnBu')
    plt.xlabel('Year')
    plt.ylabel('Genre')
    plt.title('Global Sales by Year and Genre')
    plt.show()

with tab2:
    fig = go.Figure(data=go.Heatmap(
        z=sales_by_year_genre.values,
        x=sales_by_year_genre.columns,
        y=sales_by_year_genre.index,
        colorscale='YlGnBu',
    ))
    fig.update_layout(
        title='Global Sales by Year and Genre',
        xaxis=dict(title='Year'),
        yaxis=dict(title='Genre'),
    )
    st.plotly_chart(fig)
import matplotlib.pyplot as plt
import streamlit as st
import plotly.graph_objects as go
import common

st.title("Bar Graph")

df = common.get_sales()

genre_counts = df['Genre'].value_counts().sort_values(ascending=False)

tab1, tab2 = st.tabs(["Pyplot", "Plotly"])

with tab1:
    plt.bar(genre_counts.index, genre_counts.values)
    plt.xlabel('Genre')
    plt.ylabel('Number of Games')
    plt.title('Number of Video Games by Genre')
    plt.xticks(rotation=90)
    st.pyplot(plt)

with tab2:
    fig = go.Figure(data=[go.Bar(x=genre_counts.index, y=genre_counts.values)])
    fig.update_layout(
        xaxis=dict(
            title='Genre',
            tickangle=90,
        ),
        yaxis=dict(
            title='Number of Games',
        ),
        title='Number of Video Games by Genre',
    )
    st.plotly_chart(fig)
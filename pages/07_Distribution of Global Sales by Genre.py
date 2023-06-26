import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import common

common.page_config()

st.title("Global Sales by Year and Genre")

df = common.get_sales()



tab1, tab2 = st.tabs(["Pyplot", "Plotly"])

with tab1:
    plt.boxplot(df['Global_Sales'], vert=False)
    plt.xlabel('Global Sales (in millions)')
    plt.title('Distribution of Global Sales')
    st.pyplot(plt)

with tab2:
    fig = go.Figure(data=go.Box(
        y=df['Global_Sales'],
        boxpoints='all',
        jitter=0.3,
        pointpos=-1.8,
    ))
    fig.update_layout(
        xaxis=dict(title='Global Sales (in millions)'),
        title='Distribution of Global Sales',
    )
    st.plotly_chart(fig,
                    use_container_width=True)
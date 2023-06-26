import matplotlib.pyplot as plt
import common

st.title("Bar Graph")

df = common.get_sales()

genre_counts = df['Genre'].value_counts().sort_values(ascending=False)

plt.bar(genre_counts.index, genre_counts.values)
plt.xlabel('Genre')
plt.ylabel('Number of Games')
plt.title('Number of Video Games by Genre')
plt.xticks(rotation=90)

st.pyplot(plt)
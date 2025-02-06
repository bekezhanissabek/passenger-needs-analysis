import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

df = pd.read_csv("/Users/bekezhanissabek/Desktop/Data science/passenger-needs-analytics/data/processed/topic_analysis_labeled.csv")

st.title("📊 Анализ отзывов пассажиров авиакомпаний")

# Filter for review topic
selected_topic = st.selectbox("Выберите тему:", df["topic"].unique())

filtered_df = df[df["topic"] == selected_topic]

# **1️⃣ Sentiment histogram**
st.subheader("🔍 Распределение тональности отзывов")
fig, ax = plt.subplots(figsize=(6,4))
sns.countplot(x=filtered_df["sentiment"], palette=["red", "gray", "green"], ax=ax)
plt.xlabel("Тональность")
plt.ylabel("Количество отзывов")
st.pyplot(fig)

# **2️⃣ Word cloud**
st.subheader("☁️ Самые популярные слова в отзывах")
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(" ".join(filtered_df["cleaned_review"]))
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
st.pyplot(plt)

# **3️⃣ Table with reviews**
st.subheader("📜 Примеры отзывов")
st.dataframe(filtered_df[["cleaned_review", "sentiment"]].sample(5))

# **4️⃣ Stats**
st.subheader("📈 Статистика по выбранной теме")
sentiment_counts = filtered_df["sentiment"].value_counts().reset_index()
sentiment_counts.columns = ["Тональность", "Количество"]
st.table(sentiment_counts)

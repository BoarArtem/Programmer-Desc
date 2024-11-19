import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Завантаження датасету
df = sns.load_dataset('iris')

# Назва застосунку
st.title('Демонстрація роботи з даними в Streamlit')

# Вибір колонки для відображення статистики
column = st.selectbox('Виберіть колонку для аналізу:', df.columns)

# Відображення статистики для вибраної колонки
st.write(df[column].describe())

# Створення графіку
fig, ax = plt.subplots()
sns.histplot(df[column], bins=20, ax=ax)
st.pyplot(fig)

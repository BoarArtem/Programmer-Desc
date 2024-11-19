import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Завантажуємо датасет
df = sns.load_dataset('iris')

# Додаємо заголовок
st.title('Аналіз датасету ірисів')

# Вибір виду ірису
species = st.sidebar.selectbox('Виберіть вид ірису:', df['species'].unique())

# Вибір типу графіка
plot_type = st.sidebar.radio('Виберіть тип графіка:', ['Histogram', 'Boxplot'])

# Фільтруємо датасет за видом
filtered_data = df[df['species'] == species]

# Генеруємо вибраний тип графіка
if plot_type == 'Histogram':
    fig, ax = plt.subplots()
    ax.hist(filtered_data['petal_length'], bins=20)
    st.write(f'Гістограма довжини пелюсток для {species}')
    st.pyplot(fig)
elif plot_type == 'Boxplot':
    fig, ax = plt.subplots()
    sns.boxplot(x=filtered_data['species'], y=filtered_data['petal_length'], ax=ax)
    st.write(f'Boxplot довжини пелюсток для {species}')
    st.pyplot(fig)

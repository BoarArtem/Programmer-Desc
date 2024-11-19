import streamlit as st
from PIL import Image, ImageOps
import io

st.title("Завантаження та обробка зображення")

# Завантаження зображення
uploaded_file = st.file_uploader("Виберіть зображення...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Відкриття зображення за допомогою Pillow
    image = Image.open(uploaded_file)

    # Слайдери для зміни розміру зображення
    new_width = st.slider("Виберіть нову ширину", 10, 800, image.width)
    new_height = st.slider("Виберіть нову висоту", 10, 800, image.height)

    # Зміна розміру зображення
    resized_image = image.resize((new_width, new_height))

    # Застосування чорно-білого перетворення, якщо чекбокс активний
    grayscale = st.checkbox('Перетворити на чорно-біле')
    if grayscale:
        resized_image = ImageOps.grayscale(resized_image)

    # Відображення обробленого зображення
    st.image(resized_image, caption='Оброблене зображення', use_column_width=True)

    # Кнопка для завантаження зміненого зображення
    buf = io.BytesIO()
    resized_image.save(buf, format='PNG')
    byte_im = buf.getvalue()

    st.download_button(
        label="Завантажити змінене зображення",
        data=byte_im,
        file_name="resized_image.png",
        mime="image/png"
    )


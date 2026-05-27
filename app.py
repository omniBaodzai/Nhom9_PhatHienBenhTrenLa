import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from src.utils import get_class_names, format_class_name

# Config trang
st.set_page_config(
    page_title="Phát Hiện Bệnh Trên Lá Cây",
    page_icon="🌿",
    layout="centered"
)

# Load model
@st.cache_resource
def load_disease_model():
    return load_model('models/efficientnetB0 model.keras')

model = load_disease_model()
class_names = get_class_names()

# Tiêu đề
st.title("🌿 Phát Hiện Bệnh Trên Lá Cây")

# Upload ảnh
uploaded_file = st.file_uploader(
    "Chọn ảnh lá cây cần chẩn đoán bệnh",
    type=['jpg', 'jpeg', 'png'],
    accept_multiple_files=False
)

if uploaded_file is not None:
    # Hiển thị ảnh
    img = Image.open(uploaded_file).convert('RGB')
    st.image(img, width=700)

    # Xử lý ảnh
    img_resized = img.resize((224, 224))
    img_array = np.array(img_resized)
    img_array = np.expand_dims(img_array, axis=0)

    # Dự đoán
    with st.spinner("Đang phân tích..."):
        predictions = model.predict(img_array)
        predicted_index = np.argmax(predictions[0])
        confidence = predictions[0][predicted_index] * 100

    # Hiển thị kết quả
    class_name = class_names[predicted_index]
    formatted_name = format_class_name(class_name)

    st.success(f"**Kết quả:** {formatted_name}")
    st.info(f"**Độ tin cậy:** {confidence:.2f}%")

    # Top 3 dự đoán
    st.subheader("Các bệnh khác có thể mắc:")
    top3_idx = np.argsort(predictions[0])[::-1][:3]
    for idx in top3_idx:
        name = format_class_name(class_names[idx])
        conf = predictions[0][idx] * 100
        st.progress(int(conf), text=f"{name}: {conf:.2f}%")
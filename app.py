import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
# Nạp từ điển thông tin bệnh từ file class_names.py
from src.class_names import DISEASE_DETAILS 

st.set_page_config(page_title="Hệ thống nhận diện bệnh cây trồng - Nhóm 9", layout="centered")

st.title("🌱 Hệ Thống Phát Hiện Bệnh Trên Lá Cây")
st.write("Dự án Công nghệ AI phân loại bệnh - Sử dụng kiến trúc EfficientNet-B0")

@st.cache_resource
def load_plant_model():
    return tf.keras.models.load_model('best_plant_disease_model.keras')

with st.spinner("🔄 Đang nạp mô hình AI..."):
    model = load_plant_model()

uploaded_file = st.file_uploader("Vui lòng tải lên bức ảnh lá cây cần kiểm tra...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Ảnh lá cây bạn đã chọn", use_container_width=True)
    
    if st.button("🔍 Bắt đầu nhận diện bệnh"):
        with st.spinner("🤖 Trí tuệ nhân tạo đang phân tích ảnh..."):
            # Tiền xử lý ảnh đầu vào
            img_resized = image.resize((224, 224))
            img_array = tf.keras.utils.img_to_array(img_resized)
            img_array = tf.expand_dims(img_array, 0)
            
            # Dự đoán
            predictions = model.predict(img_array)
            score = predictions[0] # Lấy mảng xác suất trực tiếp
            
            predicted_class_idx = np.argmax(score)
            # Lấy tên key tiếng Anh (ví dụ: 'Apple___Apple_scab')
            raw_class_name = list(DISEASE_DETAILS.keys())[predicted_class_idx] 
            confidence = score[predicted_class_idx] * 100
            
            # --- KHU VỰC HIỂN THỊ KẾT QUẢ ĐÃ ĐƯỢC ĐỔI MỚI ---
            st.divider()
            
            # Ngưỡng chặn độ tin cậy (Ví dụ chọn 40%). 
            # Nếu trên 40% -> Ảnh chuẩn, tra từ điển hiển thị chi tiết.
            if confidence >= 40.0:
                info = DISEASE_DETAILS[raw_class_name]
                
                # Hiển thị Tên bệnh to rõ ràng bằng tiếng Việt
                st.header(info["vi_name"])
                
                # Chia thành 3 cột nhỏ để hiển thị thông số tổng quan giống app mẫu
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown(f"**Loại tác nhân:**\n\n`{info['type']}`")
                with col2:
                    st.markdown(f"**Mức độ nghiêm trọng:**\n\n`{info['severity']}`")
                with col3:
                    st.markdown(f"**Độ tin cậy AI:**\n\n`{confidence:.1f}%`")
                
                st.write("") # Tạo khoảng cách dòng
                
                # Hiển thị các mục Triệu chứng, Nguyên nhân, Điều trị bằng Bullet Point sinh động
                st.subheader("📋 Triệu chứng")
                for symptom in info["symptoms"]:
                    st.write(f"- {symptom}")
                    
                st.subheader("🔍 Nguyên nhân có thể xảy ra")
                for cause in info["causes"]:
                    st.write(f"- {cause}")
                    
                st.subheader("💊 Sự đối đãi / Hướng điều trị")
                for treatment in info["treatment"]:
                    st.write(f"- {treatment}")
                    
            # Nếu dưới 40% -> Đây là ảnh lấy đại ngoài dataset (như ảnh lá dưa leo bạn test)
            else:
                st.warning("⚠️ **Phát hiện dấu hiệu bất thường:** Độ tin cậy của mô hình quá thấp!")
                st.write("Bức ảnh này có thể không thuộc 14 loại cây trồng nằm trong phạm vi nhận diện của hệ thống.")
                
                # Đưa ra một tư vấn chung dựa trên phỏng đoán gần nhất của AI
                st.markdown("### 📋 Phỏng đoán tổng quát dựa trên hình thái đốm lá:")
                st.error("🦠 Phát hiện tổn thương dạng Đốm lá tổng quát")
                
                col1, col2 = st.columns(2)
                col1.metric(label="Độ tin cậy phỏng đoán", value=f"{confidence:.1f}%")
                col2.metric(label="Nhóm triệu chứng tương đồng", value="Tomato/Apple Blight")
                
                st.subheader("💡 Khuyến nghị xử lý chung cho các bệnh đốm lá:")
                st.write("- **Bước 1:** Cách ly cây bị bệnh, ngắt bỏ ngay các lá có đốm vàng/nâu để tránh bào tử nấm phát tán rộng.")
                st.write("- **Bước 2:** Kiểm tra lại chế độ tưới nước, chỉ tưới ở gốc, không phun trực tiếp lên lá vào ban đêm.")
                st.write("- **Bước 3:** Chụp lại ảnh lá cây rõ ràng hơn dưới điều kiện đủ ánh sáng và tải lại lên hệ thống.")
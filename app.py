import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
# Nạp danh sách tên class từ file class_names.py kế bên
from class_names import CLASS_NAMES 

# 1. Cấu hình tiêu đề trang web hiển thị trên trình duyệt
st.set_page_config(page_title="Hệ thống nhận diện bệnh cây trồng - Nhóm 9", layout="centered")

st.title("🌱 Hệ Thống Phát Hiện Bệnh Trên Lá Cây")
st.write("Dự án Công nghệ AI phân loại bệnh - Sử dụng kiến trúc EfficientNet-B0")

# 2. Hàm tải mô hình AI vào bộ nhớ (Sử dụng cache để web không bị load lại mô hình mỗi khi bấm nút)
@st.cache_resource
def load_plant_model():
    # Tải file mô hình nằm cùng thư mục
    return tf.keras.models.load_model('best_plant_disease_model.keras')

with st.spinner("🔄 Đang nạp mô hình AI vào hệ thống, vui lòng đợi giây lát..."):
    model = load_plant_model()

# 3. Chức năng Upload ảnh của giao diện (Theo thiết kế cơ bản Tuần 4)
uploaded_file = st.file_uploader("Vui lòng tải lên bức ảnh lá cây cần kiểm tra...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Mở và hiển thị ảnh xem trước (Preview) cho người dùng nhìn thấy
    image = Image.open(uploaded_file)
    st.image(image, caption="Ảnh lá cây bạn đã chọn", use_container_width=True)
    
    # Thiết lập nút bấm kích hoạt dự đoán
    if st.button("🔍 Bắt đầu nhận diện bệnh"):
        with st.spinner("🤖 Trí tuệ nhân tạo đang phân tích ảnh..."):
            # Chuẩn hóa ảnh: Đổi kích cỡ về đúng cỡ 224x224 mà EfficientNet yêu cầu lúc train
            img_resized = image.resize((224, 224))
            img_array = tf.keras.utils.img_to_array(img_resized)
            img_array = tf.expand_dims(img_array, 0) # Tạo chiều batch (1, 224, 224, 3)
            
            # Gửi ảnh vào mô hình AI để lấy kết quả dự đoán
            predictions = model.predict(img_array)
            score = tf.nn.softmax(predictions[0]) # Dùng Softmax đổi kết quả đầu ra thành xác suất phần trăm
            
            # Tìm vị trí (index) có phần trăm độ tin cậy lớn nhất
            predicted_class_idx = np.argmax(score)
            predicted_class_name = CLASS_NAMES[predicted_class_idx]
            confidence = np.max(score) * 100
            
            # 4. Hiển thị kết quả trực quan lên màn hình (Tên bệnh & Độ tin cậy)
            st.success("🎉 Đã phân tích xong kết quả bên dưới!")
            st.metric(label="Bệnh được phát hiện / Trạng thái", value=predicted_class_name)
            st.metric(label="Độ tin cậy của mô hình", value=f"{confidence:.2f}%")
            
            # Phần hiển thị thông tin bổ sung (Mô tả, cách xử lý theo thiết kế mục tiêu)
            st.subheader("📋 Thông tin và hướng dẫn xử lý bệnh:")
            st.info("Hệ thống nhận diện thành công. Ở các bước tiếp theo, nhóm có thể kết hợp thêm từ điển để hiển thị chi tiết cách điều trị cụ thể tại đây.")
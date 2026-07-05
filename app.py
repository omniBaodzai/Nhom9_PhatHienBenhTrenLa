import streamlit as st
import os
import warnings
import textwrap

# Suppress deprecation warnings
warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="Leaf Disease Detection",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===================== CSS ======================
st.markdown("""
<style>

/* Toàn bộ nền ứng dụng: Màu sáng tự nhiên, dịu mắt, thực tế */
.stApp {
    background: #fafafa;
}

/* Ẩn menu mặc định */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Container Tiêu Đề Hệ Thống: Phong cách tối giản, gần gũi */
.header-container {
    text-align: center;
    padding: 30px 20px;
    background: #ffffff;
    border-radius: 16px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    margin-bottom: 25px;
    border: 1px solid #e0e0e0;
}

.main-title {
    font-size: 35px;
    font-weight: 700;
    color: #1b5e20; /* Màu xanh lá cây trầm phong cách nông nghiệp */
    margin-bottom: 10px;
    letter-spacing: -0.3px;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
}

.sub-title {
    color: #555555;
    font-size: 18px;
    font-weight: 400;
}

/* Biến đổi st.container(border=True) thành các Card gọn gàng */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #ffffff !important;
    border: 1px solid #e0e0e0 !important;
    border-radius: 16px !important;
    padding: 24px !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.02) !important;
}

/* Thanh Tiêu Đề Phân Khu nằm gọn gàng bên trong Card */
.custom-section-header {
    background: #CCFFFF;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 10px 16px;
    font-size: 18px;
    font-weight: 600;
    color: #424242;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 8px;
}

/* KHUNG KẾT QUẢ TOÀN DIỆN */
.result-card {
    background: #ffffff;
    border: 1px solid #e8edf2;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.02);
}

/* Tiêu đề Phân tích ảnh mẫu thiết kế lại tối giản, chuyên nghiệp hơn */
.result-card-title {
    font-size: 18px;
    font-weight: 600;
    color: #334155;
    background: #FFCC99;
    padding: 8px 14px;
    border-left: 4px solid #2e7d32;
    border-radius: 0 6px 6px 0;
    margin-bottom: 16px;
}

/* Hàng hiển thị Tên bệnh & Độ tin cậy song song */
.result-meta-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    padding: 12px 16px;
    border-radius: 8px;
    margin-bottom: 15px;
}

.result-disease-name {
    font-size: 18px;
    font-weight: 700;
    color: #166534;
}

.result-confidence {
    font-size: 18px;
    font-weight: 700;
    color: #15803d;
    background: #dcfce7;
    padding: 4px 10px;
    border-radius: 6px;
}

/* Chi tiết nội dung phân tích */
.info-section-title {
    font-size: 18px;
    font-weight: 600;
    color: #334155;
    margin-top: 14px;
    margin-bottom: 6px;
}

.info-section-content {
    font-size: 18px;
    color: #475569;
    line-height: 1.5;
    background: #f8fafc;
    padding: 12px 14px;
    border-radius: 6px;
}

/* Nút Bấm: Tone màu xanh cây cỏ thực tế */
.stButton>button {
    width: 100%;
    height: 48px;
    border-radius: 10px;
    border: none;
    background: #33FF66;
    color: #111111;
    font-size: 18px;
    font-weight: 600;
    transition: background 0.2s ease;
}

.stButton>button:hover {
    background: #1b5e20;
    color: white;
}

/* File uploader */
[data-testid="stFileUploader"] {
    border: 2px dashed #cccccc;
    border-radius: 12px;
    padding: 20px;
    background: #fafafa;
}
[data-testid="stFileUploader"]:hover {
    border-color: #2e7d32;
}

/* Tinh chỉnh các ô thông báo của Streamlit */
.stSuccess, .stError, .stInfo {
    border-radius: 10px !important;
}

/* Tối ưu khoảng cách đường gạch ngang phân đoạn */
hr {
    margin-top: 15px !important;
    margin-bottom: 25px !important;
    border-color: #e0e0e0 !important;
}

</style>
""", unsafe_allow_html=True)

# ===================== HEADER ====================

st.markdown(
    """
    <div class="header-container">
        <div class="main-title">HỆ THỐNG PHÁT HIỆN BỆNH TRÊN LÁ</div>
        <div class="sub-title">Sử dụng trí tuệ nhân tạo để chẩn đoán bệnh trên lá cây một cách nhanh chóng và chính xác</div>
    </div>
    """,
    unsafe_allow_html=True
)

selected_model = "bao_best_plant_disease_model.keras"
models_dir = "models"
model_path = os.path.join(models_dir, selected_model)

if not os.path.exists(model_path):
    st.error(f"Không tìm thấy mô hình '{selected_model}'")
else:
    col1, col2 = st.columns([1, 1], gap="large")

    # ================= LEFT: TẢI ẢNH =================
    with col1:
        with st.container(border=True):
            st.markdown('<div class="custom-section-header">Tải lên ảnh lá cây</div>', unsafe_allow_html=True)

            uploaded_files = st.file_uploader(
                "Chọn ảnh",
                type=["jpg", "jpeg", "png", "bmp", "webp"],
                accept_multiple_files=True,
                label_visibility="collapsed"
            )

            if uploaded_files:
                st.success(f"Đã tiếp nhận {len(uploaded_files)} tệp tin hình ảnh.")
                st.markdown("<br>", unsafe_allow_html=True)
                
                for i in range(0, len(uploaded_files[:10]), 2):
                    c1, c2 = st.columns(2)
                    with c1:
                        idx = i + 1
                        st.image(
                            uploaded_files[i],
                            use_container_width=True,
                            caption=f"Ảnh {idx}"
                        )
                    if i + 1 < len(uploaded_files[:10]):
                        with c2:
                            idx = i + 2
                            st.image(
                                uploaded_files[i + 1],
                                use_container_width=True,
                                caption=f"Ảnh {idx}"
                            )

    # ================= RIGHT: KẾT QUẢ CHẨN ĐOÁN =================
    with col2:
        with st.container(border=True):
            st.markdown('<div class="custom-section-header">Kết quả chẩn đoán</div>', unsafe_allow_html=True)

            if uploaded_files:
                if st.button(
                    "Tiến hành phân tích và chẩn đoán",
                    type="primary",
                    use_container_width=True
                ):
                    with st.spinner("Đang xử lý dữ liệu ảnh..."):
                        try:
                            from src.app.predict import (
                                load_trained_model,
                                predict_plant_disease
                            )

                            model = load_trained_model(model_path)

                            for idx, uploaded_file in enumerate(uploaded_files[:10], 1):
                                result = predict_plant_disease(uploaded_file, model)

                                if result["success"]:
                                    # Xử lý chuỗi dữ liệu trước khi nạp vào HTML để tránh lỗi vỡ cú pháp Markdown
                                    confidence_val = result.get('confidence', 0) * 100
                                    confidence_str = f"{confidence_val:.2f}%"
                                    disease_name = result.get('vi_name', 'Không rõ')
                                    symptom_text = result.get('symptom', 'Chưa có dữ liệu chi tiết.')
                                    treatment_text = result.get('treatment', 'Chưa có dữ liệu chi tiết.')

                                    # Tạo cấu trúc HTML và triệt tiêu toàn bộ khoảng thụt lề dòng (indentation) lỗi
                                    html_output = textwrap.dedent(f"""
                                    <div class="result-card">
                                        <div class="result-card-title">Kết quả phân tích ảnh {idx}</div>
                                        <div class="result-meta-row">
                                            <div class="result-disease-name">🌿 Tên bệnh: {disease_name}</div>
                                            <div class="result-confidence">Độ tin cậy: {confidence_str}</div>
                                        </div>
                                        <div class="info-section-title">Triệu chứng lâm sàng:</div>
                                        <div class="info-section-content">{symptom_text}</div>
                                        <div class="info-section-title">Biện pháp xử lý khuyến nghị:</div>
                                        <div class="info-section-content">{treatment_text}</div>
                                    </div>
                                    """).strip()
                                    
                                    st.markdown(html_output, unsafe_allow_html=True)
                                else:
                                    st.error(f"Hệ thống không thể đọc được cấu trúc ảnh {idx}.")

                        except Exception as e:
                            st.error(f"Hệ thống gặp sự cố: {str(e)}")
            else:
                st.info("Vui lòng tải lên ảnh để bắt đầu phân tích")
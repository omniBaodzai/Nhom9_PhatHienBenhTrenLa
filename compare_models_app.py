import streamlit as st
import os
import pandas as pd

st.set_page_config(
    page_title="Model Comparison",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📊 So sánh hiệu suất các mô hình")

st.header("🔍 So sánh Model")

models_dir = "models"
if os.path.exists(models_dir):
    model_files = [f for f in os.listdir(models_dir) if f.endswith(".keras")]
else:
    model_files = []

if not model_files:
    st.error("Không tìm thấy mô hình nào trong thư mục 'models'")
else:
    selected_models = st.multiselect(
        "Chọn các mô hình muốn đánh giá",
        model_files,
        default=model_files
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🚀 Bắt đầu đánh giá", type="primary"):
            if not selected_models:
                st.warning("Vui lòng chọn ít nhất một mô hình")
            else:
                with st.spinner("Đang đánh giá các mô hình... (có thể mất vài phút)"):
                    try:
                        from src.compare.evaluate_models import evaluate_selected_models

                        result_df, details = evaluate_selected_models(selected_models)

                        st.subheader("📈 Bảng so sánh tổng quát")
                        st.dataframe(result_df, use_container_width=True)

                        # Hiển thị Winner
                        if not result_df.empty:
                            winner = result_df.loc[result_df["F1-score"].idxmax()]
                            st.success(f"🏆 Mô hình tốt nhất: **{winner['Model']}** (F1-score: {winner['F1-score']})")

                        # Hiển thị chi tiết từng model
                        st.subheader("🔍 Chi tiết theo từng lớp bệnh")
                        for detail in details:
                            with st.expander(f"📋 {detail['Model']}"):
                                st.dataframe(detail["PerClass"], use_container_width=True)

                    except Exception as e:
                        st.error(f"Lỗi khi đánh giá mô hình: {str(e)}")
                        st.info("Kiểm tra console/terminal để xem log chi tiết.")

    with col2:
        st.info("""
        **Hướng dẫn:**
        - Chọn nhiều model để so sánh
        - Bảng đầu tiên: so sánh tổng thể
        - Mỗi expander: chi tiết đúng/sai theo từng loại bệnh
        """)

# Hệ Thống Phát Hiện Bệnh Trên Lá Cây

Ứng dụng web sử dụng AI để chẩn đoán bệnh trên lá cây từ ảnh. 


---

## 1. Tính năng chính

- Upload và phân tích 1-10 ảnh cùng lúc  
- Xác định loại bệnh với độ chính xác cao (CNN model)  
- Hiển thị triệu chứng và cách điều trị  
- Giao diện web thân thiện (Streamlit)  
- Hỗ trợ định dạng: JPG, PNG, BMP, WEBP  

---

## 2. Yêu cầu hệ thống


- **Python**: 3.8 - 3.11 (khuyến cáo 3.10)
- **Git**: Để clone repo
- **pip**: Để cài đặt dependencies

---

## 3. Hướng dẫn cài đặt

### Bước 1: Clone repository

```bash
git clone https://github.com/omniBaodzai/Nhom9_PhatHienBenhTrenLa.git
cd Nhom9_PhatHienBenhTrenLa
```

### Bước 2: Tạo virtual environment 

#### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Bước 3: Cài đặt dependencies

```bash
pip install -r requirements.txt
```

### Bước 4: Đảm bảo cấu trúc thư mục đúng

```
Nhom9_PhatHienBenhTrenLa/
├── app.py                          # File chính ứng dụng
├── requirements.txt                # Dependencies
├── README.md                        # File này
├── models/
│   └── bao_best_plant_disease_model.keras  # Model AI
├── src/
│   ├── app/
│   │   └── predict.py             # Hàm dự đoán
│   ├── common/
│   │   ├── class_names.py         # Tên các lớp bệnh
│   │   └── preprocessing.py       # Xử lý ảnh
│   └── compare/
│       └── evaluate_models.py     # So sánh model
```

---

## 4. Tải Model AI


### Tải từ Google Drive 
```
Link: https://drive.google.com/file/d/1Oe5hKUbtvw03kLspstat8agO_JGaaeV7/view?usp=sharing
1. Tải file: bao_best_plant_disease_model.keras
2. Đặt vào thư mục: models/
3. Xác nhận file tồn tại: models/bao_best_plant_disease_model.keras
```

---

## 5. Hướng dẫn sử dụng

### Chạy ứng dụng web

```bash
streamlit run app.py
```

Ứng dụng sẽ mở tại: **http://localhost:8501**

### Các bước sử dụng:

1. **Tải ảnh**: Click vào phần "Tải lên ảnh" bên trái
2. **Chọn ảnh**: Chọn 1-10 ảnh lá cây cần phân tích
3. **Xem preview**: Ảnh sẽ hiển thị 2 ảnh trên 1 hàng
4. **Phân tích**: Click nút "Phân tích ảnh" màu đỏ bên phải
5. **Xem kết quả**: 
   - Loại bệnh
   - Độ chính xác (%)
   - Triệu chứng
   - Cách điều trị

---

## License

Dự án này được phát triển cho mục đích giáo dục.

---

## Tài liệu tham khảo

- **Streamlit**: https://streamlit.io
- **TensorFlow/Keras**: https://www.tensorflow.org
- **Plant Disease Dataset**: PlantVillage Dataset
- **CNN Architecture**: EfficientNet, ResNet

---

**Cảm ơn bạn đã sử dụng hệ thống này!** 🌿

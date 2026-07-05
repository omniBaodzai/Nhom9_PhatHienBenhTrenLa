import os
import sys

import numpy as np
import tensorflow as tf

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.append(CURRENT_DIR)

from src.common.preprocessing import preprocess_image
from src.common.class_names import CLASS_INFO

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(CURRENT_DIR)))
MODEL_DEFAULT_PATH = os.path.join(BASE_DIR, "models", "bao_best_plant_disease_model.keras")


def load_trained_model(model_path=MODEL_DEFAULT_PATH):
    model_path = os.path.abspath(model_path)

    if not os.path.exists(model_path):
        raise FileNotFoundError(
            f"❌ Không tìm thấy file mô hình tại đường dẫn tuyệt đối:\n   --> {model_path}\n"
            f"Vui lòng kiểm tra lại tên file trong thư mục 'models' nhé!"
        )

    print(f"⏳ Đang nạp mô hình AI từ: {model_path}...")
    model = tf.keras.models.load_model(model_path, safe_mode=False)
    print("✅ Nạp mô hình thành công!")
    return model


def predict_plant_disease(image_input, model):
    processed_img = preprocess_image(image_input)

    if processed_img is None:
        return {"success": False, "message": "Không thể xử lý bức ảnh này."}

    predictions = model.predict(processed_img, verbose=0)
    predicted_index = int(np.argmax(predictions[0]))
    confidence = float(predictions[0][predicted_index])

    if predicted_index in CLASS_INFO:
        disease_details = CLASS_INFO[predicted_index]
        return {
            "success": True,
            "index": predicted_index,
            "confidence": confidence,
            "en_name": disease_details.get("en_name", "Unknown"),
            "vi_name": disease_details.get("vi_name", "Không rõ tên tiếng Việt"),
            "symptom": disease_details.get("symptom", "Chưa có thông tin triệu chứng."),
            "treatment": disease_details.get("treatment", "Chưa có phác đồ điều trị.")
        }
    else:
        return {
            "success": False,
            "message": f"Mô hình đoán ra mã lớp {predicted_index} nhưng lớp này chưa được định nghĩa trong class_names.py"
        }


if __name__ == "__main__":
    print("🔄 Đang chạy kiểm thử độc lập file predict.py...")
    IMAGE_TEST_PATH = "D:/Nhom9_PhatHienBenhTrenLa/test/TomatoYellowCurlVirus1.JPG"

    try:
        plant_model = load_trained_model(MODEL_DEFAULT_PATH)

        if not os.path.exists(IMAGE_TEST_PATH):
            print(f"\n💡 [GỢI Ý]: Không tìm thấy ảnh test tại đường dẫn: '{IMAGE_TEST_PATH}'.")
        else:
            result = predict_plant_disease(IMAGE_TEST_PATH, plant_model)

            if result["success"]:
                print("\n" + "=" * 60)
                print("🎯 KẾT QUẢ CHẨN ĐOÁN LÂM SÀNG TỪ AI:")
                print(f" 🔹 Lớp nhận diện (Index): {result['index']}")
                print(f" 🔹 Tên gốc (Dataset): {result['en_name']}")
                print(f" 🔹 Tên bệnh tiếng Việt: {result['vi_name']}")
                print(f" 🔹 Độ tin cậy của AI: {result['confidence'] * 100:.2f}%")
                print(f" 🔹 Triệu chứng nhận biết: \n    {result['symptom']}")
                print(f" 🔹 Phác đồ phòng chữa: \n    {result['treatment']}")
                print("=" * 60)
            else:
                print(f"❌ Dự đoán thất bại: {result['message']}")

    except Exception as error:
        print(f"❌ Đã xảy ra lỗi hệ thống: {error}")

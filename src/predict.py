import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from src.utils import get_class_names, format_class_name

IMG_SIZE = (224, 224)

def load_disease_model(model_path='models/efficientnetB0_model.keras'):
    """Load model từ file"""
    return load_model(model_path)

def preprocess_image(img_path):
    """Xử lý ảnh trước khi dự đoán"""
    img = Image.open(img_path).convert('RGB')
    img = img.resize(IMG_SIZE)
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def predict_image(model, img_path):
    """Dự đoán bệnh từ ảnh lá cây"""
    class_names = get_class_names()
    
    # Xử lý ảnh
    img_array = preprocess_image(img_path)
    
    # Dự đoán
    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions[0])
    confidence = predictions[0][predicted_index] * 100
    
    # Kết quả
    class_name = class_names[predicted_index]
    formatted_name = format_class_name(class_name)
    
    print(f"Kết quả: {formatted_name}")
    print(f"Độ tin cậy: {confidence:.2f}%")
    
    return formatted_name, confidence

def predict_top3(model, img_path):
    """Trả về top 3 dự đoán"""
    class_names = get_class_names()
    img_array = preprocess_image(img_path)
    predictions = model.predict(img_array)
    
    top3_idx = np.argsort(predictions[0])[::-1][:3]
    results = []
    for idx in top3_idx:
        name = format_class_name(class_names[idx])
        conf = predictions[0][idx] * 100
        results.append((name, conf))
    
    return results


if __name__ == "__main__":
    # Test thử
    model = load_disease_model()
    # predict_image(model, 'path/to/image.jpg')
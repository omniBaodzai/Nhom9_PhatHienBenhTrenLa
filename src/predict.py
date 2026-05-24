import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

IMG_SIZE = (224, 224)

def predict_image(model_path, img_path, class_names):
    """Dự đoán bệnh từ ảnh lá cây"""
    model = load_model(model_path)

    img = Image.open(img_path).convert('RGB')
    img = img.resize(IMG_SIZE)
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions[0])
    confidence = predictions[0][predicted_index] * 100

    print(f"Kết quả: {class_names[predicted_index]}")
    print(f"Độ tin cậy: {confidence:.2f}%")

    return class_names[predicted_index], confidence
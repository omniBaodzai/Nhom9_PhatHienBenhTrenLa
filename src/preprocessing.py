import numpy as np
from PIL import Image

IMG_SIZE = (224, 224)

def preprocess_image(img):
    """
    Xử lý 1 ảnh trước khi đưa vào model
    Input: PIL Image hoặc đường dẫn file
    Output: numpy array shape (1, 224, 224, 3)
    """
    if isinstance(img, str):
        img = Image.open(img)
    
    img = img.convert('RGB')
    img = img.resize(IMG_SIZE)
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    
    return img_array

def preprocess_batch(img_paths):
    """
    Xử lý nhiều ảnh cùng lúc
    Input: list đường dẫn ảnh
    Output: numpy array shape (n, 224, 224, 3)
    """
    batch = []
    for path in img_paths:
        img = Image.open(path).convert('RGB')
        img = img.resize(IMG_SIZE)
        batch.append(np.array(img))
    
    return np.array(batch)

def validate_image(img_path):
    """
    Kiểm tra ảnh có hợp lệ không
    """
    try:
        img = Image.open(img_path)
        img.verify()
        return True
    except Exception:
        return False
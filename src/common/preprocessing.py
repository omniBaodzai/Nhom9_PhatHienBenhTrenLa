import os
from io import BytesIO

import numpy as np
from PIL import Image


def preprocess_image(image_input, target_size=(224, 224)):
    """
    Hàm tiền xử lý ảnh đầu vào cho mô hình.
    """
    try:
        if isinstance(image_input, (str, os.PathLike)):
            img = Image.open(image_input)
        elif hasattr(image_input, "getvalue"):
            img_bytes = image_input.getvalue()
            img = Image.open(BytesIO(img_bytes))
        elif hasattr(image_input, "read"):
            if hasattr(image_input, "seek"):
                image_input.seek(0)
            img_bytes = image_input.read()
            img = Image.open(BytesIO(img_bytes))
        else:
            img = image_input

        if hasattr(img, "mode") and img.mode != "RGB":
            img = img.convert("RGB")

        img = img.resize(target_size)
        img_array = np.array(img).astype("float32")
        img_array /= 255.0
        img_array = np.expand_dims(img_array, axis=0)

        return img_array

    except Exception as e:
        print(f"❌ Đã xảy ra lỗi trong quá trình xử lý ảnh: {e}")
        return None

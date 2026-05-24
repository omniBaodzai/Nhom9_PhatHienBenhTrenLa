import os
import shutil
from PIL import Image

IMG_SIZE = (224, 224)

def resize_images(input_dir, output_dir):
    """Resize ảnh về 224x224 và lưu vào output_dir"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    classes = os.listdir(input_dir)
    for cls in classes:
        cls_input = os.path.join(input_dir, cls)
        cls_output = os.path.join(output_dir, cls)
        os.makedirs(cls_output, exist_ok=True)

        for img_name in os.listdir(cls_input):
            img_path = os.path.join(cls_input, img_name)
            try:
                img = Image.open(img_path).convert('RGB')
                img = img.resize(IMG_SIZE)
                img.save(os.path.join(cls_output, img_name))
            except Exception as e:
                print(f"Lỗi ảnh {img_name}: {e}")

    print(f"Resize xong! Lưu tại: {output_dir}")
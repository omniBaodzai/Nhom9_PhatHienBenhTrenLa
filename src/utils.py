import os
import matplotlib.pyplot as plt

def plot_training_history(history, save_path='training_history.png'):
    """Vẽ biểu đồ loss và accuracy sau khi train"""
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    # Loss
    axes[0].plot(history.history['loss'], label='train loss')
    axes[0].plot(history.history['val_loss'], label='val loss')
    axes[0].set_title('Loss')
    axes[0].set_xlabel('Epoch')
    axes[0].legend()

    # Accuracy
    axes[1].plot(history.history['accuracy'], label='train accuracy')
    axes[1].plot(history.history['val_accuracy'], label='val accuracy')
    axes[1].set_title('Accuracy')
    axes[1].set_xlabel('Epoch')
    axes[1].legend()

    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()
    print(f"Đã lưu biểu đồ tại: {save_path}")

def get_class_names(data_dir):
    """Lấy danh sách tên class từ thư mục"""
    return sorted(os.listdir(data_dir))

def print_class_distribution(data_dir):
    """In số lượng ảnh mỗi class"""
    classes = get_class_names(data_dir)
    print(f"Tổng số class: {len(classes)}")
    for cls in classes:
        count = len(os.listdir(os.path.join(data_dir, cls)))
        print(f"  {cls}: {count} ảnh")
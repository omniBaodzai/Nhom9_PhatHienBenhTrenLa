import os
import sys
from collections import defaultdict

import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.append(CURRENT_DIR)

from src.app.predict import load_trained_model, predict_plant_disease

BASE_DIR = os.path.dirname(os.path.dirname(CURRENT_DIR))
MODELS_DIR = os.path.join(BASE_DIR, "models")
TEST_DIR = os.path.join(BASE_DIR, "test")


def load_test_dataset(test_dir=TEST_DIR):
    image_paths = []
    true_labels = []

    if not os.path.exists(test_dir):
        raise FileNotFoundError(f"Không tìm thấy thư mục test: {test_dir}")

    for class_name in sorted(os.listdir(test_dir)):
        class_dir = os.path.join(test_dir, class_name)
        if not os.path.isdir(class_dir):
            continue

        for image_name in os.listdir(class_dir):
            if image_name.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".webp")):
                image_paths.append(os.path.join(class_dir, image_name))
                true_labels.append(class_name)

    return image_paths, true_labels


def evaluate_model(model_name, model_path, test_dir=TEST_DIR, show_detail=False):
    print("\n" + "=" * 70)
    print(f"MODEL: {model_name}")
    print("=" * 70)

    if not os.path.exists(model_path):
        print(f"❌ Không tìm thấy model: {model_path}")
        return None

    model = load_trained_model(model_path)
    image_paths, true_labels = load_test_dataset(test_dir)

    y_true = []
    y_pred = []
    correct = 0
    class_stats = defaultdict(lambda: {"correct": 0, "total": 0})

    for idx, image_path in enumerate(image_paths):
        true_label = true_labels[idx]
        result = predict_plant_disease(image_path, model)

        if result["success"]:
            pred_label = result["en_name"]
            y_true.append(true_label)
            y_pred.append(pred_label)

            class_stats[true_label]["total"] += 1
            if pred_label == true_label:
                correct += 1
                class_stats[true_label]["correct"] += 1

            if show_detail:
                status = "✅ CORRECT" if pred_label == true_label else "❌ WRONG"
                print(f"{os.path.basename(image_path):<50} | True: {true_label:<35} | Pred: {pred_label:<35} | {status}")

    if not y_true:
        print("Không có ảnh nào được dự đoán thành công.")
        return None

    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average="weighted", zero_division=0)
    recall = recall_score(y_true, y_pred, average="weighted", zero_division=0)
    f1 = f1_score(y_true, y_pred, average="weighted", zero_division=0)

    print("\n" + "=" * 70)
    print(f"SUMMARY - {model_name}")
    print("=" * 70)
    print(f"Correct : {correct}/{len(y_true)}")
    print(f"Accuracy: {accuracy * 100:.2f}%")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1-score : {f1:.4f}")

    print("\n" + "=" * 70)
    print(f"PER-CLASS PERFORMANCE - {model_name}")
    print("=" * 70)

    class_rows = []
    for cls, stats in sorted(class_stats.items()):
        total = stats["total"]
        correct_cls = stats["correct"]
        acc = round((correct_cls / total * 100), 2) if total > 0 else 0.0
        class_rows.append({
            "Disease Class": cls,
            "Total": total,
            "Correct": correct_cls,
            "Wrong": total - correct_cls,
            "Accuracy (%)": acc
        })

    class_df = pd.DataFrame(class_rows)
    print(class_df.to_string(index=False))

    return {
        "Model": model_name,
        "Accuracy (%)": round(accuracy * 100, 2),
        "Precision": round(precision, 4),
        "Recall": round(recall, 4),
        "F1-score": round(f1, 4),
        "PerClass": class_df
    }


def evaluate_selected_models(selected_models, test_dir=TEST_DIR):
    results = []
    details = []

    for model_file in selected_models:
        model_path = os.path.join(MODELS_DIR, model_file)
        model_name = os.path.splitext(model_file)[0]

        metrics = evaluate_model(model_name, model_path, test_dir, show_detail=False)
        if metrics:
            results.append(metrics)
            details.append(metrics)

    if not results:
        return pd.DataFrame(), []

    summary_df = pd.DataFrame([{
        "Model": r["Model"],
        "Accuracy (%)": r["Accuracy (%)"],
        "Precision": r["Precision"],
        "Recall": r["Recall"],
        "F1-score": r["F1-score"]
    } for r in results])

    return summary_df, details


if __name__ == "__main__":
    print("=" * 80)
    print("LEAF DISEASE MODEL EVALUATION")
    print("=" * 80)

    model_files = [f for f in os.listdir(MODELS_DIR) if f.endswith(".keras")]

    if not model_files:
        print("❌ Không tìm thấy file model nào trong thư mục models/")
        sys.exit(1)

    result_df, _ = evaluate_selected_models(model_files, TEST_DIR)

    print("\n" + "=" * 80)
    print("MODEL COMPARISON")
    print("=" * 80)
    print(result_df.to_string(index=False))

    if not result_df.empty:
        winner = result_df.loc[result_df["F1-score"].idxmax()]
        print(f"\n🏆 WINNER: {winner['Model']} (F1-score: {winner['F1-score']})")

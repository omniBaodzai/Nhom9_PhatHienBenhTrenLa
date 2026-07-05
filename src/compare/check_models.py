import os
import tensorflow as tf

MODELS = [
    "models/baseline_cnn.keras",
    "models/best_plant_disease_model.keras",
    "models/efficientnet_finetuned.keras"
]


def check_models():
    for path in MODELS:
        print("\n" + "=" * 60)
        print(path)

        model = tf.keras.models.load_model(path, safe_mode=False)

        print("Input :", model.input_shape)
        print("Output:", model.output_shape)
        print("Params:", f"{model.count_params():,}")
        print("\nLast layer:")
        print(model.layers[-1])

        print("=" * 60)

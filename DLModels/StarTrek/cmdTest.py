import argparse
import numpy as np
import tensorflow as tf
from tensorflow import keras
import sys
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

class StarTrekPredictor:
    def __init__(self, model_path):
        # load model
        print(f" load model from {model_path}...")
        try:
            self.model = keras.models.load_model(model_path)
            self.class_names = ['commandRed', 'operationGold', 'scienceBlue']
            print(" model loaded")
        except Exception as e:
            print(f" error loading model: {e}")
            sys.exit(1)

    def preprocess_image(self, image_path):
        """
        Loads and preprocesses a single image to match training conditions.
        """
        try:
            # load file, decode img and resize to model's input - 128x128
            img = tf.io.read_file(image_path)
            img = tf.image.decode_image(img, channels=3, expand_animations=False)
            img = tf.image.resize(img, (128, 128))
            # standardize to match model & add batch dimension 
            img = img / 255.0
            img = tf.expand_dims(img, axis=0)
            return img
        except Exception as e:
            print(f"error processing image: {e}")
            return None

    def predict(self, image_path):
        """Runs inference and returns the result."""
        processed_img = self.preprocess_image(image_path)
        if processed_img is None:
            return

        # run pred and decode result
        predictions = self.model.predict(processed_img, verbose=0)
        confidence = 100 * np.max(predictions[0])
        class_idx = np.argmax(predictions[0])
        class_name = self.class_names[class_idx]

        return class_name, confidence


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Star Trek Uniform Classifier CLI")
    parser.add_argument("image", help="Path to the image file")
    parser.add_argument("--model", default="custom_model_stclassifier.keras", help="Path to .keras model file")
    
    args = parser.parse_args()

    # init and pred
    predictor = StarTrekPredictor(args.model)
    result = predictor.predict(args.image)
    
    if result:
        label, conf = result
        print("\n" + "="*30)
        print(f"PREDICTION: {label.upper()}")
        print(f"CONFIDENCE: {conf:.2f}%")
        print("="*30 + "\n")

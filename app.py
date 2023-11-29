from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
import os
import logging

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)

# Confirm the current working directory and the existence of the model file
model_path = 'OPT_LSTM_model1.keras'  # Update this if your model is in a different path
app.logger.info(f"Current working directory: {os.getcwd()}")
if os.path.exists(model_path):
    app.logger.info(f"Found model file at {model_path}")
else:
    app.logger.error(f"Model file not found at {model_path}")

# Load model with error handling
try:
    model = tf.keras.models.load_model(model_path)
    app.logger.info("Model loaded successfully.")
except Exception as e:
    app.logger.error(f"Error loading the model: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_text():
    try:
        data = request.get_json(force=True)
        input_text = data['text']
        prediction = model.predict(np.array([input_text]))  # Adjust for model's expected input format
        return jsonify({'prediction': float(prediction[0])})
    except Exception as e:
        app.logger.error(f"Error during prediction: {e}")
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify, render_template
import tensorflow as tf
from keras.preprocessing.text import tokenizer_from_json
from keras.preprocessing.sequence import pad_sequences
import keras
import numpy as np
import os
import logging
import json

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)

# Parameters
total_vocabulary = 5000
max_len = 100

# Load the tokenizer
with open('vocabulary_tokenizer.json', 'r') as f:
    tokenizer_config = f.read()
tokenizer = keras.preprocessing.text.tokenizer_from_json(tokenizer_config)

# Load the model
model_path = 'SA_Trained_Model.h5'
try:
    model = keras.models.load_model(model_path)
    app.logger.info("Model loaded successfully.")
except Exception as e:
    app.logger.error(f"Error loading the model: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])  # Changed from '/analyze' to '/predict'
def analyze_text():
    try:
        data = request.get_json(force=True)
        input_text = data['text']
        app.logger.info(f"Received text: {input_text}")
        input_seq = pad_sequences(tokenizer.texts_to_sequences([input_text]), padding='post', maxlen=max_len)
        prediction = model.predict(input_seq)
        app.logger.info(f"Prediction: {prediction}")
        return jsonify({'prediction': float(prediction[0])})
    except Exception as e:
        app.logger.error(f"Error during prediction: {e}")
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

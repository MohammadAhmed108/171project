from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
import keras

app = Flask(__name__)
model = keras.models.load_model('OPT_LSTM_model.keras')  # Load  model

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_text():
    data = request.get_json(force=True)
    input_text = data['text']
    prediction = model.predict(np.array([input_text]))  # Use the model to predict
    return jsonify({'prediction': float(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)

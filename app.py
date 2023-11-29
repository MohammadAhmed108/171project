from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Exception handling for model loading
try:
    model = tf.keras.models.load_model('C:/Users/Affan/OneDrive - Rebel Hosting/Desktop/171 group project/OPT_LSTM_model.keras.url')  # Ensure this path is correct
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading the model: {e}")

@app.route('/')
def home():
    # Ensure that 'templates/index.html' exists
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_text():
    try:
        data = request.get_json(force=True)
        input_text = data['text']
        # Preprocess input_text here if necessary
        prediction = model.predict(np.array([input_text]))  # Use the model to predict
        # Ensure prediction is in the correct format to be sent as JSON
        return jsonify({'prediction': float(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

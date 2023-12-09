function submitText() {
    const text = document.getElementById('textInput').value;
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: text }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('predictionResult').innerText = 'Prediction: ' + data.prediction;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
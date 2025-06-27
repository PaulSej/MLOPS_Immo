from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('best_model.pkl')

@app.route('/predict', methods=['GET'])
def predict():
    data = request.json
    prediction = model.predict([data['features']])
    return jsonify({'predicted_price': prediction[0]})


if __name__ == '__main__':
    app.run()
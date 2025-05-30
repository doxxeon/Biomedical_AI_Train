# server.py

from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load('lgbm_clf.pkl')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])
    prediction = model.predict(df)

    return jsonify({'prediction': prediction.tolist()})

def hi():
    return 'hi'

if __name__ == '__main__':
    app.run('127.0.0.1', port=9999, debug=True)
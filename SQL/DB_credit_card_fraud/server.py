from flask import Flask, request, jsonify
import joblib
import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime

app = Flask(__name__)

# 모델 불러오기
model = joblib.load('lgbm_clf.pkl')

# DB 연결 (여기 본인 정보 넣기)
engine = create_engine("mysql+pymysql://root:doxxeon@127.0.0.1:3306/mydb")
# 예시: "mysql+pymysql://root:1234@127.0.0.1:3306/fraud_db"

# 테이블 없으면 생성 (깔끔하게 정의)
with engine.connect() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            prediction INT,
            predicted_at DATETIME
        )
    """))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])
    prediction = model.predict(df)

    # 예측 결과 추가
    prediction_result = pd.DataFrame({
        'prediction': prediction,
        'predicted_at': [datetime.now()] * len(prediction)
    })

    # DB에 저장
    prediction_result.to_sql('predictions', con=engine, if_exists='append', index=False, method='multi')

    # 예측 결과 반환
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run('127.0.0.1', port=9999, debug=True)
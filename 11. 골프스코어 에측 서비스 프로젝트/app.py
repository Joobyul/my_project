from flask import Flask, render_template, request
import os  # os 모듈 추가
import joblib
import pandas as pd


app = Flask(__name__)

# 모델 파일의 경로
model_path = './project/rf_model.pkl'  # 모델 파일의 경로를 설정해주세요

# joblib을 사용하여 모델 불러오기
model = joblib.load(model_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # 사용자 입력 데이터를 받아오기
    features = [float(request.form['페어웨이안착률']),
                float(request.form['드라이브거리']),
                float(request.form['평균퍼팅']),
                float(request.form['그린적중률']),
                float(request.form['벙커세이브율']),
                float(request.form['리커버리율']),
                float(request.form['평균버디'])]

    # 입력 데이터를 DataFrame으로 변환
    input_data = pd.DataFrame([features], columns=['페어웨이안착률', '드라이브거리', '평균퍼팅', '그린적중률', '벙커세이브율', '리커버리율', '평균버디'])

    # 모델을 사용하여 예측
    predicted_result = model.predict(input_data)

    # 예측 결과를 HTML 템플릿에 전달
    return render_template('result.html', prediction=predicted_result[0])

if __name__ == '__main__':
    app.run(debug=True)


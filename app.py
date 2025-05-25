import os
import json
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/receive-data', methods=['POST'])
def receive_data():
    data = request.get_json()

    # 로그 출력
    print("받은 데이터:", data)

    # 저장할 경로
    log_path = "carbon_log.json"

    # 타임스탬프 추가
    data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 파일에 한 줄씩 저장
    with open(log_path, "a") as f:
        f.write(json.dumps(data) + "\n")

    return jsonify({"status": "success"}), 200

@app.route('/')
def home():
    return 'Carbon 서버 작동중임'


@app.route('/status')
def status():
    return "서버 정상 동작 중입니다"

from flask import Flask, jsonify
import subprocess


app = Flask(__name__)


@app.route('/gps', methods=['GET'])
def capture_image():
    try:
        # 여기에서 라즈베리 파이에서 카메라를 제어하는 Python 코드 실행
        result = subprocess.check_output(['python3', 'gps.py'])
        
        return jsonify(result=result)
    except Exception as e:
        return jsonify(result=str(e))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
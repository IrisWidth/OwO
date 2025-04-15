from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/save-ip', methods=['POST'])
def save_ip():
    ip = request.json.get('ip')
    time = datetime.datetime.now().isoformat()
    with open('ip_log.txt', 'a') as f:
        f.write(f"IP: {ip}, Czas: {time}\n")
    return 'IP zapisane pomyślnie!'

if __name__ == '__main__':
    app.run(debug=True)
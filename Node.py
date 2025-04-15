from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/save-ip', methods=['POST'])
def save_ip():
    ip = request.json.get('ip')
    if ip:
        time = datetime.datetime.now().isoformat()
        try:
            with open('ip_log.txt', 'a') as f:
                f.write(f"IP: {ip}, Czas: {time}\n")
            return 'IP zapisane pomyślnie!'
        except Exception as e:
            return f'Błąd zapisu do pliku: {e}', 500
    return 'Brak adresu IP w żądaniu!', 400

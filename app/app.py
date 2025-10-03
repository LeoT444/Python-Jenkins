from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/status')
def status():
    return jsonify({"status": "ok", "message": "API funcionando!"})

@app.route('/api/hello/<name>')
def hello(name):
    return jsonify({"message": f"Olá, {name}!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
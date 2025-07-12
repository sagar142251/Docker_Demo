from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello from Flask using Multi-Stage Docker Build!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

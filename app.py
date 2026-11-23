from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! My application is running through Jenkins CI/CD."

@app.route('/health')
def health():
    return "Application is Healthy - OK", 200

@app.route('/info')
def info():
    return {
        "application": "Jenkins Demo Application",
        "version": "1.0",
        "environment": "local"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
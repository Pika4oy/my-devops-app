from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Привет, DevOps! pika4oy в деле! 🚀</h1><p>CI/CD + Docker + GitHub Actions</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

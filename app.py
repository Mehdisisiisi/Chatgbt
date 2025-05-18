from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, I am your AI Assistant!"

if __name__ == "__main__":
    app.run()

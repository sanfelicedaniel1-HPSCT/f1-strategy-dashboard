from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Scuderia San Felice is live!"

if __name__ == '__main__':
    app.run()
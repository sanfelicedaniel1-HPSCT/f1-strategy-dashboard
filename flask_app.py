from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/live')
def live():
    return render_template('live.html')

@app.route('/historical')
def historical():
    return render_template('historical.html')

if __name__ == '__main__':
    app.run(debug=True)
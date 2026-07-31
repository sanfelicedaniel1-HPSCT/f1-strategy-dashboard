from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Serves the main landing page portal."""
    return render_template('index.html')

@app.route('/live')
def live():
    """Serves the live timing & telemetry hub."""
    return render_template('live.html')

@app.route('/historical')
def historical():
    """Serves the historical post-race vault analytics engine."""
    return render_template('historical.html')

if __name__ == '__main__':
    app.run(debug=True)
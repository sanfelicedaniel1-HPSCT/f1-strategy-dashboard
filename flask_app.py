from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def live():
    """Serves the Live / Countdown Dashboard"""
    return render_template("live.html")

@app.route("/historical")
def historical():
    """Serves the Historical Race Data Vault"""
    return render_template("historical.html")

if __name__ == "__main__":
    app.run(debug=True)
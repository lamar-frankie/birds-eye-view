from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/status')
def status():
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return "Mood.af lives " + time_stamp


if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, render_template
import json

app = Flask(__name__)

def load_couples():
    with open("couples.json", "r") as f:
        return json.load(f)

@app.route("/")
def home():
    couples = load_couples()
    return render_template("index.html", couples=couples)
@app.route("/status/<status_filter>")

def filter_by_status(status_filter):
    couples = load_couples()
    filtered = [c for c in couples if c["status"].lower() == status_filter.lower()]
    return render_template("index.html", couples=filtered)

if __name__ == "__main__":
    app.run(debug=True)

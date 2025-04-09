from flask import Flask, render_template
import json

app = Flask(__name__)

def load_couples():
    with open("couples.json", "r") as f:
        return json.load(f)

@app.route("/")
def home():
    data = load_couples()
    seasons = data["seasons"]
    return render_template("index.html", seasons=seasons)

@app.route("/status/<status_filter>")
def filter_by_status(status_filter):
    data = load_couples()
    # Flatten all couples into one list for status filtering
    all_couples = []
    for season in data["seasons"]:
        for couple in season["couples"]:
            if couple["status"].lower() == status_filter.lower():
                all_couples.append(couple)
    return render_template("index.html", seasons=[{
        "season": f"Filtered: {status_filter.title()}",
        "show": "All Shows",
        "couples": all_couples
    }])

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

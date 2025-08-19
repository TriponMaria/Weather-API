from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]



@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())


if __name__ == "__main__":
    app.run(debug=True)


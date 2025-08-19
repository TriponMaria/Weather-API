from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]



@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())

@app.route("/api/<station>/<date>")
def station_specific_date(station, date):
    filename = f"data_small/TG_STAID{str(station).zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == f"{date}"]["   TG"].squeeze() / 10
    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }

@app.route("/api/<station>")
def station_data(station):
    filename = f"data_small/TG_STAID{station.zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    results = df.to_dict(orient="records")
    return results

@app.route("/api/yearly/<station>/<year>")
def yearly(station, year):
    filename = f"data_small/TG_STAID{station.zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    results = []
    print(year)
    records = df.to_dict(orient="records")
    for record in records:
        if str(record["    DATE"].year) == str(year):
            results.append(record)
    return results


if __name__ == "__main__":
    app.run(debug=True)


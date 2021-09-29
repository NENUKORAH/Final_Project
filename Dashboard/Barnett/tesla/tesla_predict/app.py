# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from .models import Day


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


# Query the database and send the jsonified results
@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        hdate = request.form["dayhdate"]
        hopen = request.form["dayhdate"]
        hhigh = request.form["dayhhigh"]
        hlow = request.form["dayhlow"]
        hclose = request.form["dayhclose"]
        hvolume = request.form["dayhvolume"]

        day = Day(ticker="TSLA", hdate=hdate, hhigh=hhigh, hlow=hlow, hclose=hclose, hvolume=hvolume)
        db.session.add(day)
        db.session.commit()
        return redirect("/", code=302)

    return render_template("form.html")


@app.route("/api/days")
def days():
    results = db.session.query(Day.hdate, Day.hopen, Day.hhigh, Day.hlow, Day.hclose, Day.hvolume).all()

    hover_text = [result[0] for result in results]
    hdate = [result[1] for result in results]
    hopen = [result[2] for result in results]
    hhigh = [result[3] for result in results]
    hlow = [result[4] for result in results]
    hclose = [result[5] for result in results]
    hvolume = [result[6] for result in results]

    #day_data = [{
    #    "type": "scattergeo",
    #    "locationmode": "USA-states",
    #    "lat": lat,
    #    "lon": lon,
    #    "text": hover_text,
    #    "hoverinfo": "text",
    #    "marker": {
    #       "color": ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'],
    #        "size": 15,
    #        "line": {
    #            "color": "rgb(8,8,8)",
    #            "width": 1
    #        },
    #    }
    #}]

    return jsonify(day_data)


if __name__ == "__main__":
    app.run()

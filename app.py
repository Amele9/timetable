from flask import Flask, render_template, request

from timetable import get_timetable

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/timetable", methods=["POST"])
def timetable() -> str:
    return render_template("timetable.html", timetable=get_timetable(
        request.form["start_lesson_numbers"],
        request.form["lessons"]
    ))

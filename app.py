from flask import Flask, render_template, request, url_for, redirect

import db

app = Flask(__name__)


@app.route("/")
def index():
    detail = db.find_detail_date()

    return render_template("index.html", detail=detail)


@app.route("/add", methods=["GET", "POST"])
def add_detail_date():
    if request.method == "GET":
        return render_template("status.html")

    if request.method == "POST":
        userid = request.form["userid"]
        date = request.form["date"]
        behavior = request.form["behavior"]
        winlose = request.form["winlose"]

        db.add_detail_date(userid, date, behavior, winlose)

        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)

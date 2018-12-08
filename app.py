from flask import Flask, render_template, request, url_for, redirect

import db

app = Flask(__name__)


# ホーム
@app.route("/index")
def index():
    detail = db.find_detail_date()
    goal = db.find_goal()

    return render_template("index.html", detail=detail, goal=goal)


# 行動記録
@app.route("/add", methods=["GET", "POST"])
def add_detail_date():
    if request.method == "GET":
        goal = db.find_goal()
        return render_template("status.html", goal=goal)

    if request.method == "POST":
        userid = request.form["userid"]
        date = request.form["date"]
        behavior = request.form["behavior"]
        winlose = request.form["winlose"]

        db.add_detail_date(userid, date, behavior, winlose)

        return redirect(url_for("index"))


# 目標記録
@app.route("/", methods=["GET", "POST"])
def add_goal():
    if request.method == "GET":
        goal = db.find_goal()
        return render_template("first.html", goal=goal)

    if request.method == "POST":
        userid = request.form["userid"]
        goal = request.form["goal"]

        db.add_goal(userid, goal)

        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)

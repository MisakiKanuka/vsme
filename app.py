from flask import Flask, render_template, request, url_for, redirect

import db

app = Flask(__name__)


# ホーム
@app.route("/index")
def index():
    detail = db.find_detail_date()
    goal = db.find_goal()

    return render_template("index.html", detail=detail, goal=goal)


# 勝数カウント
@app.route("/result")
def show_result():
    cnt_win = db.find_win()
    cnt_lose = db.find_lose()
    goal = db.find_goal()

    return render_template("result.html", cnt_win=cnt_win, cnt_lose=cnt_lose, goal=goal)


# 行動記録
@app.route("/add", methods=["GET", "POST"])
def add_detail_date():
    if request.method == "GET":
        goal = db.find_goal()
        return render_template("status.html", goal=goal)

    if request.method == "POST":
        userid = request.form["userid"]
        behavior = request.form["behavior"]
        winlose = request.form["winlose"]

        db.add_detail_date(userid, behavior, winlose)

        return redirect("/result")


# 目標記録
@app.route("/goal", methods=["GET", "POST"])
def add_goal():
    if request.method == "GET":
        goal = db.find_goal()
        return render_template("first.html", goal=goal)

    if request.method == "POST":
        userid = request.form["userid"]
        goal = request.form["goal"]

        db.add_goal(userid, goal)

        return redirect(url_for("index"))


# ユーザー登録
@app.route("/", methods=["GET", "POST"])
def create_user():
    if request.method == "GET":
        users_info = db.find_user()
        return render_template("login.html", users_info=users_info)

    if request.method == "POST":
        userid = request.form["userid"]
        name = request.form["name"]
        password = request.form["password"]

        db.create_user(userid, name, password)

        return redirect(url_for("add_goal"))


if __name__ == "__main__":
    app.run(debug=True)

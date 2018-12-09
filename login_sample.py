import flask
import flask_login

app = flask.Flask(__name__)

app.secret_key = "secret"
login_manager = flask_login.LoginManager()

login_manager.init_app(app)

# mock database
users = {
    "Bob": {"password": "b"},
    "Tom": {"password": "t"}
}


class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(username):
    if username not in users:
        return
    user = User()
    user.id = username
    return user


@app.route("/login", methods=["GET", "POST"])
def login():
    if flask.request.method == "GET":
        return flask.render_template("login_sample.html")

    username = flask.request.form["username"]
    if flask.request.form["password"] == users[username]["password"]:
        user = User()
        user.id = username

        # ログインする
        flask_login.login_user(user)

        return flask.redirect(flask.url_for("protected"))

    return "Bad login"


@app.route("/logout")
def logout():
    flask_login.logout_user()

    return flask.redirect(flask.url_for("login"))


@app.route("/protected")
@flask_login.login_required  # 認証したい場合はデコレーション
def protected():
    return flask.render_template("protected.html")


if __name__ == "__main__":
    app.run(debug=True)

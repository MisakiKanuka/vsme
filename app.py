from flask import Flask, render_template

import db

app = Flask(__name__)


@app.route("/")
def index():
    detail = db.find_detail_data()

    return render_template("index.html", detail=detail)




if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import render_template


app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    return render_template("www/index.html")


@app.route("/<name>", methods=["GET"])
def show_name(name):
    return escape(name), 200


@app.route("/<int:age>", methods=["GET"])
def show_age(age):
    return "Idade: %d" % age, 200


@app.get("/path/<path:subpath>")
def show_subpath(subpath):
    return f"Subpath {escape(subpath)}"


@app.get("/uuid/<uuid:id>")
def show_uuid(id):
    return f"uuid {escape(id)}"


with app.test_request_context():
    print(url_for("show_name", name="Helder"))
    print(url_for("show_age", age=27))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

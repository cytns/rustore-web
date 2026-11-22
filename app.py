import sqlite3
from pathlib import Path

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    connection = sqlite3.connect(Path(__file__).parent / "apps.db")
    connection.row_factory = sqlite3.Row
    apps = connection.execute("SELECT * FROM apps ORDER BY id").fetchall()
    connection.close()

    return render_template("index.html", apps=apps)


if __name__ == "__main__":
    app.run()

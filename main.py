from flask import Flask
from utils import *


app = Flask(__name__)


@app.route("/")
def page_index():
    return show_candidates()


@app.route("/candidates/<x>")
def eeeueuuuu_index(x):
    return show_pictures(x)


@app.route("/skills/<x>")
def by_skills(x):
    return get_by_skill(x)


if __name__ == "__main__":
    app.run()
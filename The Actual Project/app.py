from flask import Flask, render_template
from pathlib import Path
from db import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.instance_path = Path(".").resolve() 

db.init_app(app) 

@app.route("/")
def home(): 
    return render_template("home.html", name="tim")

if __name__ == "__main__": 
    app.run(debug=True, port=8888) 
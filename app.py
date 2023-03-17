from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.secret_key = "Foodtoe"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Data(db.Model):
    name = db.Column(db.String(100), primary_key = True)
    ID = db.Column(db.Integer)
    points = db.Column(db.Integer)

    def __init__(self, name, ID, points):
        self.name = name
        self.ID = ID
        self.points = points

@app.route('/')
def Index():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
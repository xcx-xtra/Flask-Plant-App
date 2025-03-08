from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default='Incomplete')
    date = db.Column(db.String(20), nullable=False)
    rating = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Plant {self.title}>'